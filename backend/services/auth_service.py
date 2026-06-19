from schemas import auth
from sqlalchemy.orm import Session
from models.users import User
from fastapi import HTTPException, status
from pwdlib import PasswordHash
from sqlalchemy import or_


def register_user(body:auth.RegisterRequest, db: Session):
    ## 1. username and email should be unique
    existing_user = db.query(User).filter( 
        or_(User.username == body.username,
            User.email == body.email)
             ).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")
    
    ## 2. Validate Password strength (at least 8 characters, contains letters and numbers), username should be alphanumeric and between 3-50 characters
    if( len(body.password) < 8 or 
        not any(c.isalpha() for c in body.password) or 
        not any(c.isdigit() for c in body.password)):
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long and contain both letters and numbers")
    
    if(len(body.username)<3 or len(body.username)>50 or not body.username.isalnum()):
        raise HTTPException(status_code=400, detail="Username must be alphanumeric and between 3 to 50 characters long")
    
    ## 3. Hash the password before storing 
    password_hasher =PasswordHash.recommended()

    hashed_password = password_hasher.hash(body.password)


    ## 4. create user
    new_user = User(
        username = body.username,
        full_name = body.full_name,
        email = body.email,
        phone_number = body.phone_number,
        hashed_password = hashed_password, 
        role = body.role
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception:
        db.rollback()
        raise 
    return new_user
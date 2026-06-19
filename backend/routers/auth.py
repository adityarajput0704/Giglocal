from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import auth
from database import get_db
from services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=auth.UserResponse, status_code=status.HTTP_201_CREATED)
def register(body:auth.RegisterRequest, db: Session = Depends(get_db)):
    return auth_service.register_user(body, db)
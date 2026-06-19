from pydantic import BaseModel, EmailStr, Field
from uuid import UUID
import enum

class UserRole(str, enum.Enum):
    HOMEOWNER = "homeowner"
    WORKER = "worker"

class RegisterRequest(BaseModel):
    full_name: str = Field(..., min_length=1, max_length=100)
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    phone_number: str = Field(..., min_length=10, max_length=15)
    role : UserRole = Field(..., description="User role, either 'homeowner' or 'worker'")
    password: str = Field(..., min_length=8, max_length=128)

    
class LoginRequest(BaseModel):
    identifier: str = Field(..., description="Username or email")
    password: str = Field(..., min_length=8, max_length=128)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: UUID
    username: str
    full_name: str
    email: EmailStr
    phone_number: str
    role: UserRole
    is_active: bool

class LoginResponse(BaseModel):
    user : UserResponse
    access_token: str
    token_type: str = "bearer"
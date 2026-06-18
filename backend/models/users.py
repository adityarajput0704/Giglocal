from sqlalchemy import Column, String, Boolean, Enum, Timestamp
from sqlalchemy.dialects.postgresql import UUID
from backend.database import Base
import enum, uuid


class UserRole(enum.Enum):
    HOMEOWNER = "homeowner"
    WORKER = "worker"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.HOMEOWNER)
    is_active = Column(Boolean, default=True)
    created_at = Column(Timestamp(timezone=True), nullable=False)


from sqlalchemy import Column, String, Boolean, Enum, DateTime
from datetime import datetime, UTC
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import enum, uuid


class UserRole(enum.Enum):
    HOMEOWNER = "homeowner"
    WORKER = "worker"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.HOMEOWNER)
    is_active = Column(Boolean, default=True)
    created_at = Column(
         DateTime(timezone=True),
         default=datetime.now(UTC),
         nullable=False
    )
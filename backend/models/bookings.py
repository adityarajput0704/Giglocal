from sqlalchemy import Column, DateTime, String, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime, UTC
from database import Base
import enum, uuid



class BookingStatus(enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Bookings(Base):
    __tablename__ = "bookings"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    stripe_payment_intent_id = Column(String, nullable=False)
    status = Column(Enum(BookingStatus), nullable=False, default=BookingStatus.PENDING)
    created_at = Column(
         DateTime(timezone=True),
         default=datetime.now,
         nullable=False
    )


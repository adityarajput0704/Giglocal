from sqlalchemy import Column, String, ForeignKey, Enum, Timestamp
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from backend.database import Base
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
    created_at = Column(Timestamp(timezone=True), nullable=False)


from sqlalchemy import Column, Integer, Text, ForeignKey, Enum, Numeric
from sqlalchemy.dialects.postgresql import UUID
from database import Base
import enum, uuid


class QuoteStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class JobQuote(Base):
    __tablename__ = "job_quotes"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    job_id = Column(UUID(as_uuid=True), ForeignKey("jobs.id"), nullable=False)
    worker_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    price = Column(Numeric(10, 2), nullable=False)
    estimated_duration_min= Column(Integer, nullable=False)
    message = Column(Text, nullable=True)
    status = Column(Enum(QuoteStatus), nullable=False, default=QuoteStatus.PENDING)
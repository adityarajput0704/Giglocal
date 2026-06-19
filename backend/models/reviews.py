from sqlalchemy import Column, Text, ForeignKey, SmallInteger
from database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Review(Base):
    __tablename__ = "reviews"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    reviewer_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    booking_id = Column(UUID(as_uuid=True), ForeignKey("bookings.id"), nullable=False)
    rating = Column(SmallInteger, nullable=False)
    comment = Column(Text, nullable=True)
    
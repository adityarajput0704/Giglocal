from sqlalchemy import Column, Text, ForeignKey, Enum, Numeric, Timestamp
from sqlalchemy.dialects.postgresql import UUID
from backend.database import Base
import enum, uuid
from geoalchemy2 import Geography


class JobStatus(enum.Enum):
    OPEN = "open"
    ASSIGNED = "assigned"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class UrgencyLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class Jobs(Base):
    __tablename__ = "jobs"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    homeowner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    category = Column
    description = Column(Text, nullable=False)
    location = Column(
        Geography(
            geometry_type="POINT",
            srid=4326
        ),
        nullable=False
    )
    status = Column(Enum(JobStatus), nullable=False, default=JobStatus.OPEN)
    urgency = Column(Enum(UrgencyLevel), nullable=False, default=UrgencyLevel.MEDIUM)

    ai_price_low = Column(Numeric(10, 2), nullable=True)
    ai_price_high = Column(Numeric(10, 2), nullable=True)
    expired_at = Column(Timestamp(timezone=True), nullable=False)
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Float, Numeric
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from database import Base
import enum, uuid
from geoalchemy2 import Geography


class AvailabilityStatus(enum.Enum):
    AVAILABLE = "available"
    BUSY = "busy"
    OFFLINE = "offline"

class WorkerProfile(Base):
    __tablename__ = "worker_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    location = Column(
        Geography(
            geometry_type="POINT",
            srid=4326
        ),
        nullable=False
    )

    skills = Column(ARRAY(String), nullable=False)

    availability_status = Column(
            Enum(AvailabilityStatus),
            nullable=False,
            default=AvailabilityStatus.AVAILABLE
        )
    
    hourly_rate = Column(Numeric(10, 2), nullable=False)
    ranking_score = Column(Float, nullable=False, default=0.0)

from sqlalchemy import Column, Integer, ForeignKey, String, Numeric
from database import Base


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id"),
        nullable=False
    )

    stripe_charge_id = Column(
        String,
        unique=True
    )

    amount = Column(
        Numeric(10, 2),
        nullable=False
    )

    commission = Column(
        Numeric(10, 2),
        nullable=False,
        default=0
    )

    payout_id = Column(String)
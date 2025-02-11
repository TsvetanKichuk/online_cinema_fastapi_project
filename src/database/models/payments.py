from enum import Enum

from sqlalchemy import Enum as SQLAlchemyEnum, ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base


class PaymentsStatusEnum(str, Enum):
    PENDING = "pending payments"
    PAID = "payed payments"

class PaymentsTypeEnum(str, Enum):
    PAYMENT = "payment"
    FINE = "fine"

class PaymentsModel(Base):
    __tablename__ = "payments"

    status: Mapped[PaymentsStatusEnum] = mapped_column(
        SQLAlchemyEnum(PaymentsStatusEnum), nullable=False
    )
    type: Mapped[PaymentsTypeEnum] = mapped_column(
        SQLAlchemyEnum(PaymentsTypeEnum), nullable=False
    )
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    session_url: Mapped[str] = mapped_column(String(255))
    session_id: Mapped[int] = mapped_column(primary_key=True)
    money_to_pay: Mapped[float] = mapped_column(nullable=False)


    def __str__(self):
        return f"{self.status}, {self.type}, {self.borrowing_id}"

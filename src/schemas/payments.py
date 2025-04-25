from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveFloat, Field


class PaymentCreateSchema(BaseModel):
    order_id: int = Field(description="Payment ID")
    amount: PositiveFloat = Field(description="Amount")
    payment_date: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Payment date")
    payment_method: str = Field(description="Card or cash payments")

    def validate_payment(self):
        """Check amount, must be positive."""
        if self.amount <= 0:
            raise ValueError("Amount must be positive")


class PaymentResponseSchema(BaseModel):
    id: int
    order_id: int
    amount: PositiveFloat
    payment_date: datetime
    payment_method: str

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, PositiveFloat


class PaymentCreateSchema(BaseModel):
    order_id: int = Field(description="ID заказа, к которому относится платеж")
    amount: PositiveFloat = Field(description="Сумма платежа")
    payment_date: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Дата платежа")
    payment_method: str = Field(description="Метод оплаты (например, карта, наличные)")

    def validate_payment(self):
        """Проверяет, чтобы сумма платежа была положительной."""
        if self.amount <= 0:
            raise ValueError("Сумма платежа должна быть положительной")


class PaymentResponseSchema(BaseModel):
    id: int
    order_id: int
    amount: PositiveFloat
    payment_date: datetime
    payment_method: str

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, PositiveFloat


class OrderItem(BaseModel):
    movie_id: int
    quantity: int = Field(gt=0, description="Количество товара")
    price: PositiveFloat = Field(description="Цена за единицу товара")


class OrderCreateSchema(BaseModel):
    customer_id: int = Field(description="ID клиента")
    items: List[OrderItem] = Field(description="Список товаров")
    order_date: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Дата заказа")
    total_price: Optional[float] = Field(default=None, description="Общая стоимость заказа")

    def calculate_total_price(self):
        """Подсчитает общую стоимость заказа."""
        self.total_price = sum(item.quantity * item.price for item in self.items)


class OrderResponseSchema(BaseModel):
    id: int
    customer_id: int
    items: List[OrderItem]
    order_date: datetime
    total_price: float

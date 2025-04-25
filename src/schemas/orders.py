from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, PositiveFloat


class OrderItem(BaseModel):
    movie_id: int
    quantity: int = Field(gt=0, description="Count of goodness")
    price: PositiveFloat = Field(description="Price of goodness")


class OrderCreateSchema(BaseModel):
    customer_id: int = Field(description="Client ID")
    items: List[OrderItem] = Field(description="List of OrderItems")
    order_date: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Order date")
    total_price: Optional[float] = Field(default=None, description="Total price")

    def calculate_total_price(self):
        """Calculate total price"""
        self.total_price = sum(item.quantity * item.price for item in self.items)


class OrderResponseSchema(BaseModel):
    id: int
    customer_id: int
    items: List[OrderItem]
    order_date: datetime
    total_price: float

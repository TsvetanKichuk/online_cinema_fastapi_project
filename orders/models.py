from pydantic import BaseModel
from typing import List, Optional

from user.models import UserModel


class Ticket(Base):
    __tablename__ = "tickets"
    movie_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seat_number: Mapped[int] = mapped_column(Integer)
    showtime: Mapped[str] = mapped_column(String(255))

class OrderRequest(BaseModel):
    __tablename__ = "orders"

    customer_id: Mapped[UserModel] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tickets: Mapped[List["Ticket"]] = relationship("Ticket")
    total_price: Mapped[float] = mapped_column(Float)
    # Add other order details as needed (e.g., payment info)

class OrderResponse(BaseModel):
    order_id: int # Unique ID for the order
    total_price: float
    tickets: List[Ticket]
    # ... other relevant information

class AvailableMovies(BaseModel):
    movies: List[dict] # Example: [{"id": 1, "title": "Movie A"}, {"id": 2, "title": "Movie B"}]

class ErrorResponse(BaseModel):
    detail: str

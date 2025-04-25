from typing import List

from sqlalchemy import Integer, String, Float, UniqueConstraint, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from src.database.models.accounts import UserModel
from src.database.models.base import Base


class Ticket(Base):
    __tablename__ = "tickets"
    movie_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    seat_number: Mapped[int] = mapped_column(Integer)
    showtime: Mapped[str] = mapped_column(String(255))

class OrderRequest(Base):
    __tablename__ = "orders"

    customer_id: Mapped[UserModel] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tickets: Mapped[List["Ticket"]] = relationship("Ticket")
    total_price: Mapped[float] = mapped_column(Float)

    __table_args__ = (
        UniqueConstraint("tickets_id", "customer_id", name="unique_ticket_constraint"),
    )

class OrderResponse(Base):
    order_id: Mapped[int] = mapped_column(Integer) # Unique ID for the order
    total_price: Mapped[float] = mapped_column(Float)
    tickets: Mapped[List[Ticket]] = mapped_column(ForeignKey("tickets.movie_id"))

class AvailableMovies(Base):
    movies: List[dict]

class ErrorResponse(Base):
    detail: str

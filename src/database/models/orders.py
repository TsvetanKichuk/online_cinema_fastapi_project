from pydantic import BaseModel
from typing import List, Optional

class Ticket(BaseModel):
    movie_id: int
    seat_number: str
    showtime: str

class OrderRequest(BaseModel):
    customer_id: int
    tickets: List[Ticket]
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
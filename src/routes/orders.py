from fastapi import APIRouter, HTTPException, Depends
from .models import OrderRequest, OrderResponse, AvailableMovies, ErrorResponse
from database.services import OrderService  # We'll create this service class

router = APIRouter()
order_service = OrderService() # Initialize the service

@router.post("/create", response_model=OrderResponse, responses={400: {"model": ErrorResponse}})
async def create_order(order_request: OrderRequest):
    try:
        order = order_service.create_order(order_request)
        return order
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/movies", response_model=AvailableMovies)
async def get_available_movies():
    movies = order_service.get_available_movies() # Example
    return AvailableMovies(movies=movies)

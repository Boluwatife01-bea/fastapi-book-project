from fastapi import APIRouter

# Import your new books.py file
from api.books import router as books_router

api_router = APIRouter()

# Include the books router
api_router.include_router(books_router, prefix="/api/v1/books", tags=["books"])

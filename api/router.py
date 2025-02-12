from fastapi import APIRouter

# Import books route from api/routes
from api.routes.books import router as books_router

api_router = APIRouter()

# Register books API under /api/v1/books
api_router.include_router(books_router, prefix="/books", tags=["books"])

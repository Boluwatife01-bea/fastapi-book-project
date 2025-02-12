from fastapi import APIRouter, HTTPException
from typing import Dict

router = APIRouter()

# Sample book database (replace with actual DB later)
books_db: Dict[int, Dict] = {
    1: {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    2: {"id": 2, "title": "1984", "author": "George Orwell"},
    3: {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
}

@router.get("/{book_id}")
def get_book(book_id: int):
    """Retrieve a book by its ID"""
    if book_id not in books_db:
        raise HTTPException(status_code=404, detail="Book not found")
    return books_db[book_id]

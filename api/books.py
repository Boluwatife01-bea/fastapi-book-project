from fastapi import APIRouter, HTTPException

router = APIRouter()

# Fake book data (Replace with database query if needed)
books = {
    1: {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    2: {"id": 2, "title": "1984", "author": "George Orwell"},
}

@router.get("/api/v1/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

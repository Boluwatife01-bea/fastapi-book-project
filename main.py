from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import api_router
from api import books  # Import the books router
from core.config import settings

app = FastAPI()

# CORS Middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all API routes
app.include_router(api_router, prefix=settings.API_PREFIX)
app.include_router(books.router)  # Register books API

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}

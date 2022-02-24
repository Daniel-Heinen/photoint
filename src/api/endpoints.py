"""API endpoints"""
from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "healthy"}
# Modified 2024-07-01
# Modified 2025-09-02

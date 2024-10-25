"""Data models for location"""
from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float
    confidence: float
# Modified 2024-07-05
# Modified 2024-10-25

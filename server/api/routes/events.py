from fastapi import APIRouter
from database.repository import get_events

router = APIRouter()

@router.get("/events")
def fetch_events():
    data = get_events()
    return {"events": data}
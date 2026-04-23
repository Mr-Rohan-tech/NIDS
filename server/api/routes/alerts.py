from fastapi import APIRouter
from database.repository import get_alerts

router = APIRouter()

@router.get("/alerts")
def fetch_alerts():
    data = get_alerts()
    return {"alerts": data}
from fastapi import APIRouter, BackgroundTasks
from core.engine import process_event

router = APIRouter()

@router.post("/")
async def ingest_event(event: dict, bg: BackgroundTasks):
    bg.add_task(process_event, event)
    return {"status": "processing"}
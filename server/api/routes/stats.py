from fastapi import APIRouter
from database.db import get_connection

router = APIRouter()


@router.get("/")
def get_stats():
    conn = get_connection()
    cursor = conn.cursor()

    # Total events
    cursor.execute("SELECT COUNT(*) FROM events")
    result_events = cursor.fetchone()
    total_events = result_events[0] if result_events else 0

    # Total alerts
    cursor.execute("SELECT COUNT(*) FROM alerts")
    result_alerts = cursor.fetchone()
    total_alerts = result_alerts[0] if result_alerts else 0

    cursor.close()
    conn.close()

    return {
        "total_events": total_events,
        "total_alerts": total_alerts
    }
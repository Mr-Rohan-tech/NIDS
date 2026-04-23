from fastapi import APIRouter
from api.routes import ingest
from api.routes.events import router as events_router
from api.routes.alerts import router as alerts_router
from api.routes.stats import router as stats_router

router = APIRouter()

# Attach sub-routes to router
router.include_router(ingest.router, prefix="/ingest", tags=["Ingest"])
router.include_router(stats_router, prefix="/stats", tags=["Stats"])
router.include_router(events_router, prefix="/events", tags=["Events"])
router.include_router(alerts_router, prefix="/alerts", tags=["Alerts"])
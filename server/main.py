from fastapi import FastAPI
from api.server import router as api_router
from api.auth import router as auth_router   # ✅ ADD THIS
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    app = FastAPI(title="IDS System")

    # Existing routes
    app.include_router(api_router, prefix="/api")

    # 🔥 ADD THIS (IMPORTANT)
    app.include_router(auth_router, prefix="/api")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = create_app()
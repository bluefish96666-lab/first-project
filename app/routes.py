from fastapi import APIRouter

from app.config import get_settings


router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@router.get("/health")
def health_check() -> dict[str, str]:
    settings = get_settings()
    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.app_env,
    }

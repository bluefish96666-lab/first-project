from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello from FastAPI"}


@router.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

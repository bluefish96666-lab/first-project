from fastapi import FastAPI

from app.routes import router


app = FastAPI(
    title="Python Web Project",
    version="0.1.0",
    description="A minimal FastAPI starter project.",
)

app.include_router(router)

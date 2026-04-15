from fastapi import FastAPI

from app.config import get_settings
from app.logging_config import configure_logging
from app.middleware import RequestContextMiddleware
from app.routes import router


def create_app() -> FastAPI:
    settings = get_settings()
    configure_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        description="A minimal FastAPI starter project.",
    )
    app.add_middleware(RequestContextMiddleware)
    app.include_router(router)
    app.state.settings = settings
    return app


app = create_app()

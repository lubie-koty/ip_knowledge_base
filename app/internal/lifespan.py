import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.internal.config import settings
from app.internal.setup import create_knowledge_base, load_knowledge_base_file

logger = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):
    filename = settings.knowledge_base_filename
    logger.info(f"Loading knowledge base from file: {filename}")
    try:
        data = load_knowledge_base_file(filename)
    except FileNotFoundError:
        logger.error(f"Could not load knowledge base from file: {filename}")
        raise
    app.state.knowledge_base = create_knowledge_base(data)
    yield

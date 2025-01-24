from fastapi import FastAPI

from app.internal.lifespan import lifespan
from app.routers import ip_tags


app = FastAPI(lifespan=lifespan)
app.include_router(ip_tags.router)

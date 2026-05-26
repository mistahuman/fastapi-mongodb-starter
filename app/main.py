from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import AsyncMongoClient
from beanie import init_beanie
import logging
import uvicorn

from app.conf.config import setup_advanced_logging, Config
from app.models.exampleitem import ExampleItem
from app.routers import exampleitem

conf_logger = setup_advanced_logging()
logger = logging.getLogger("main")


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncMongoClient(Config.app_settings["mongodb_url"])
    await init_beanie(
        database=client[Config.app_settings["db_name"]],
        document_models=[ExampleItem],
    )
    logger.info("Beanie initialized")
    yield
    await client.aclose()


app = FastAPI(
    title=Config.title,
    version=Config.version,
    redirect_slashes=False,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.app_settings.get("cors_origins", ["*"]),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exampleitem.router, tags=["exampleitems"])


@app.get("/")
def root():
    return {"msg": f"Hello {Config.title or 'World'}!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

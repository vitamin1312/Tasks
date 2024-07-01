from fastapi import FastAPI
from contextlib import asynccontextmanager

from router import router as tasks_router
from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('database is empty')
    await create_tables()
    print('database is ready to work')
    yield
    print('shutdown')

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

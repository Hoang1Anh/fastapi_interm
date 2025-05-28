from click import command
from fastapi import FastAPI
from alembic.config import Config
from .database import Base, engine
from .router import files, morse_decoder

app = FastAPI(title="File Storage System")


Base.metadata.create_all(bind=engine)

app.include_router(files.router)

app.include_router(morse_decoder.router)




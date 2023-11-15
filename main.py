from fastapi import FastAPI
from Models import Register
from Router import router

app = FastAPI()

app.include_router(router)
from fastapi import FastAPI
from api.routes import videoupload, url, chat, health

app = FastAPI(title="Video RAG API")

app.include_router(videoupload.router)
app.include_router(url.router)
app.include_router(chat.router)
app.include_router(health.router)
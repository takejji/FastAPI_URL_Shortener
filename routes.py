from fastapi import APIRouter

from app import url_shortener

routes = APIRouter()

routes.include_router(url_shortener.router, prefix="/app")
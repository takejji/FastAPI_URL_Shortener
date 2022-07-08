from fastapi import APIRouter, Request

from .service import cut_link


router = APIRouter()


@router.get("/generate/v2/{url}")
async def url_generator(url: str, request: Request):
    link = cut_link()
    return {'full url': url, 'short url': f"{request.url.hostname}/{link}"}

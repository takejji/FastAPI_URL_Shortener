from fastapi import FastAPI

from routes import routes


app = FastAPI()


app.include_router(router=routes)

#
# @app.get("/generate/{url}")
# async def generate_url(url: str, item: GeneratorUrl):
#     return {'url': url, 'item': item}
#
#
# @app.get('/check/{short_url}')
# async def check_url(short_url: str):
#     return {'short url': short_url}

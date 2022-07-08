from fastapi import FastAPI

app = FastAPI()


@app.get("/generate/{url}")
async def generate_url(url: str):
    return {'url': url}


@app.get('/check/{short_url}')
async def check_url(short_url: str):
    return {'short url': short_url}

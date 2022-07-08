from pydantic import BaseModel


class GeneratorUrl(BaseModel):
    url: str
    short_url: str

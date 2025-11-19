from pydantic import BaseModel


class ResponseInfo(BaseModel):
    app_name: str
    version: str

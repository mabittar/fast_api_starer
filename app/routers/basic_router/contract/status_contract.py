from typing import Optional
from pydantic import BaseModel, Field


class StatusResponseModel(BaseModel):
    api: str = Field(..., description="API Name", example="entrance")
    id: int = Field(..., description="Interface Id", example=123456)
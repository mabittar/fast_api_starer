
from pydantic import BaseModel, Field


class StatusResponseModel(BaseModel):
    api: str = Field(..., description="API Name", example="FastAPI starter")
    msg: str = Field(..., description="Test Message", example="Welcome")

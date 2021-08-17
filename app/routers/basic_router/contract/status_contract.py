
from pydantic import BaseModel, Field


class StatusResponseModel(BaseModel):
    api: str = Field(..., description="API Name", example="FastAPI starter")
    id: int = Field(..., description="Interface Id", example=123456)
    msg: str = Field(..., description="Test Message", example="Welcome")

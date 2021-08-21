
from pydantic import BaseModel, Field

from model.common import IDModelMixin


class StatusResponseModel(IDModelMixin):
    api: str = Field(..., description="API Name", example="FastAPI starter")
    msg: str = Field(..., description="Test Message", example="Welcome")

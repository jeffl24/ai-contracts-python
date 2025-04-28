from pydantic import BaseModel
from typing import Optional

class Contract(BaseModel):
    id: Optional[str]
    filename: str
    intellectual_properties: str
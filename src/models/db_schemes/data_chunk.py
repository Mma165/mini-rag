from pydantic import BaseModel, Field
from typing import Optional
from bson.objectid import ObjectId
class DataChunk(BaseModel):
    id : Optional[ObjectId]= Field(None,alias="_id")
    chunk_txt: Optional[str]=Field(..., min_length=1)
    chunk_metadata: Optional[dict]
    chunk_order: Optional[int] =Field(..., ge=0)
    chunk_project_id: Optional[ObjectId] = Field(..., min_length=1)

    class Config:
        arbitrary_types_allowed = True

from pydantic import BaseModel,ConfigDict

class TableBase(BaseModel):
    name: str
    seats: int
    location: str

class TableCreate(TableBase):
    pass

class TableRead(TableBase):
    id: int

    class Config:
       model_config = ConfigDict(from_attributes=True)
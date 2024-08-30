from pydantic import BaseModel

class Tasks(BaseModel):
    id: int
    name: str
    author_id: int

class TaskAdd(BaseModel):
    name: str
    author_id: int
    

class DeleteSchema(BaseModel):
    message: str
    
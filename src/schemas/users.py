from pydantic import BaseModel


class Users(BaseModel):
    id: int
    name: str

class UserAdd(BaseModel):
    name: str
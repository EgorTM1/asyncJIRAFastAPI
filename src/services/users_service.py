from typing import List
from src.utils.repository import SQLAlchemyRepository
from src.models.users_model import UsersModel
from src.schemas.users import UserAdd, Users
from src.schemas.tasks import DeleteSchema


class UsersService(SQLAlchemyRepository):
    model = UsersModel


    async def add_user(self, data: UserAdd) -> int:
        info = data.model_dump()

        result = await super().add_one(info)

        return result
    

    async def get_users(self) -> List[Users]:
        result = await super().find_all()

        return result
    

    async def delete_user(self, id: int) -> DeleteSchema:
        result = await super().delete_one(id)

        return result
    
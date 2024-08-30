from typing import List
from fastapi import APIRouter
from src.schemas.tasks import DeleteSchema
from src.schemas.users import Users, UserAdd
from src.services.users_service import UsersService


router_users = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router_users.get('')
async def get_users() -> List[Users]:
    result = await UsersService().get_users()

    return result 


@router_users.post('')
async def add_user(data: UserAdd) -> int:
    result = await UsersService().add_user(data)

    return result


@router_users.delete('/{id}')
async def delete_user(id: int) -> DeleteSchema:
    result = await UsersService().delete_user(id)

    return result
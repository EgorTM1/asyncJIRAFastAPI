from typing import List
from fastapi import APIRouter
from src.services.tasks_service import TasksService
from src.schemas.tasks import DeleteSchema, TaskAdd, Tasks


router_tasks = APIRouter(prefix='/tasks', tags=['Tasks'])


@router_tasks.get('')
async def get_tasks() -> List[Tasks]:
    result = await TasksService().get_tasks()

    return result


@router_tasks.post('')
async def add_task(data: TaskAdd) -> int:
    result = await TasksService().add_task(data)

    return result


@router_tasks.delete('/{id}')
async def delete_task(id: int) -> DeleteSchema:
    result = await TasksService().delete_task(id)

    return result

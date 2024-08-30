from typing import List
from src.utils.repository import SQLAlchemyRepository
from src.models.tasks_model import TasksModel
from src.schemas.tasks import DeleteSchema, TaskAdd, Tasks


class TasksService(SQLAlchemyRepository):
    model = TasksModel

    async def add_task(self, data: TaskAdd) -> int:
        info = data.model_dump()

        res_id = await super().add_one(info)

        return res_id
    
    async def get_tasks(self) -> List[Tasks]:
        result = await super().find_all()

        return result
    
    async def delete_task(self, id: int) -> DeleteSchema:
        result = await super().delete_one(id)

        return result

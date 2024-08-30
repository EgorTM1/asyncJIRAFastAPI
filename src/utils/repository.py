from typing import List
from sqlalchemy import select
from abc import ABC, abstractmethod
from src.db.db import async_session_maker
from src.schemas.tasks import Tasks, DeleteSchema


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    

    @abstractmethod
    async def find_all():
        raise NotImplementedError
    

    @abstractmethod
    async def delete_one():
        raise NotImplementedError
    


class SQLAlchemyRepository(AbstractRepository):
    model = None


    async def add_one(self, data: dict) -> int:
        async with async_session_maker() as session:
            add_obj = self.model(**data)

            session.add(add_obj)
            session.flush()
            await session.commit()

            return add_obj.id
        
    
    async def find_all(self) -> List[Tasks]:
        async with async_session_maker() as session:
            query = select(self.model)

            res = await session.execute(query)
            result = [row[0].to_read_model() for row in res.all()]

            return result
        

    async def delete_one(self, id: int) -> DeleteSchema:
        async with async_session_maker() as session:
            del_obj = await session.get(self.model, id)

            await session.delete(del_obj)
            await session.commit()

            return {'message': 'Good!'}
        
        
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from src.db.db import Base
from src.schemas.tasks import Tasks


class TasksModel(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))


    def to_read_model(self) -> Tasks:
        return Tasks(
            id=self.id,
            name=self.name,
            author_id=self.author_id
        )
    
    
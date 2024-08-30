from sqlalchemy.orm import Mapped, mapped_column
from src.db.db import Base
from src.schemas.users import Users

class UsersModel(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    def to_read_model(self) -> Users:
        return Users(
            id=self.id,
            name=self.name
        )
    
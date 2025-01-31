from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from application.interfaces.user_repository import UserRepository
from domain.entities.user import User, UserId
from infrastructure.database.models.user import UserModel


class SQLUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @staticmethod
    async def _model_to_entity(model: UserModel) -> User:
        return User(
            id=UserId(model.id),
            email=model.email,
            hashed_password=model.hashed_password,
            is_active=model.is_active,
        )

    async def get_by_id(self, user_id: UserId) -> User | None:
        result = await self.session.scalar(select(User).where(User.id == user_id))
        return await self._model_to_entity(result) if result else None

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.scalar(
            select(UserModel).where(UserModel.email == email)
        )
        return await self._model_to_entity(result) if result else None

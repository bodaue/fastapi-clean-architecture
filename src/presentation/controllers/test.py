from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from infrastructure.database.models.user import UserModel

router = APIRouter()


@router.get("/test")
@inject
async def test(session: FromDishka[AsyncSession]) -> dict[str, str]:
    await session.get(UserModel, 1)
    return {"Hello": "World"}

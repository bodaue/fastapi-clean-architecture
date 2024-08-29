from typing import Any

from fastapi import APIRouter

router = APIRouter()


@router.get("/test")
async def test() -> dict[str, Any]:
    return {"message": "Hello, World!"}

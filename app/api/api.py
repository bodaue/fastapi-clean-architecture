from fastapi import APIRouter

from app.api.routes import test

router = APIRouter(prefix="/api/v1")
router.include_router(test.router, tags=["Test"])

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import router
from app.config import settings

app = FastAPI(
    title=settings.common.title,
    debug=settings.common.debug,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.server.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.server.host, port=settings.server.port)

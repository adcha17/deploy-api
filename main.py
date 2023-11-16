from fastapi import FastAPI

from app.v1.router.deploy import router as deploy_router

app = FastAPI()

app.include_router(deploy_router)

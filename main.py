from fastapi import FastAPI
from src.api.routes.verify import router

app = FastAPI(title="Nexus Verify API")
app.include_router(router)

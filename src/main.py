from fastapi import FastAPI
from routes import base_router, data_router
from helpers import get_settings
from motor.motor_asyncio import AsyncIOMotorClient 
app = FastAPI() 
@app.on_event("startup")
async def startup_db_client():
    settings=get_settings()
    app.mongodb_connection = AsyncIOMotorClient(settings.MongoDB_URI)
    app.mongodb_client = app.mongodb_connection[settings.MongoDB_Database]
@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_connection.close() 

app.include_router(base_router)
app.include_router(data_router)


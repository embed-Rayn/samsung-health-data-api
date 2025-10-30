from fastapi import APIRouter
from app.models import SleepRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploadjson/sleep")
async def upload_sleep(data: SleepRequest):
    return data_service.save_data(data)
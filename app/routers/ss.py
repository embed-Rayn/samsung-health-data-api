from fastapi import APIRouter
from app.models import SleepSessionRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/ss")
async def upload_sleep_session(data: SleepSessionRequest):
    return data_service.save_data(data)
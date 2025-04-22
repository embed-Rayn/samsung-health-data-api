from fastapi import APIRouter
from app.models import HeartRateRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/hr")
async def upload_heart_rate(data: HeartRateRequest):
    return data_service.save_data(data)
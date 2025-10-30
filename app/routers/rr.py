from fastapi import APIRouter
from app.models import RespiratoryRateRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploadjson/respiratory_rate")
async def upload_respiratory_rate(data: RespiratoryRateRequest):
    return data_service.save_data(data)

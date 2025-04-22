from fastapi import APIRouter
from app.models import StepDailyRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/sd")
async def upload_step_daily(data: StepDailyRequest):
    return data_service.save_data(data)
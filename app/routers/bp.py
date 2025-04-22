from fastapi import APIRouter
from app.models import BloodPressureRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/bp")
async def upload_blood_pressure(data: BloodPressureRequest):
    return data_service.save_data(data)
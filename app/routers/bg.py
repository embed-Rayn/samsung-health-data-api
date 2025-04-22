from fastapi import APIRouter
from app.models import BloodGlucoseRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/bg")
async def upload_blood_glucose(data: BloodGlucoseRequest):
    return data_service.save_data(data)
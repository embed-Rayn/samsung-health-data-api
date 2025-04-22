from fastapi import APIRouter
from app.models import BloodOxygenRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/bo")
async def upload_blood_oxygen(data: BloodOxygenRequest):
    return data_service.save_data(data)
from fastapi import APIRouter
from app.models import SkinTemperatureRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploaddata/st")
async def upload_skin_temperature(data: SkinTemperatureRequest):
    return data_service.save_data(data)
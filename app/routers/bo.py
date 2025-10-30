from fastapi import APIRouter
from app.models import OxygenSaturationRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploadjson/oxygen_saturation")
async def upload_oxygen_saturation(data: OxygenSaturationRequest):
    return data_service.save_data(data)
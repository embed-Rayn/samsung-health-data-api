from fastapi import APIRouter
from app.models import HRVRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploadjson/hrv")
async def upload_hrv(data: HRVRequest):
    return data_service.save_data(data)

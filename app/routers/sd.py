from fastapi import APIRouter
from app.models import StepRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploadjson/step")
async def upload_step(data: StepRequest):
    return data_service.save_data(data)
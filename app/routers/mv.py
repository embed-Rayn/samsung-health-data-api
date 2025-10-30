from fastapi import APIRouter
from app.models import MovementRequest
from app.services import data_service

router = APIRouter()

@router.post("/app/smc_uploadjson/movement")
async def upload_movement(data: MovementRequest):
    return data_service.save_data(data)

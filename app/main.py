from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import st, bp, bg, bo, hr, ss, sd, rr, hrv, mv

app = FastAPI()

# CORS 미들웨어 설정 - 대용량 요청 처리를 위한 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 필요에 따라 특정 도메인으로 제한 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 기본 엔드포인트
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 각 데이터 타입별 라우터 등록
app.include_router(st.router)   # Skin Temperature
app.include_router(bp.router)   # Blood Pressure  
app.include_router(bg.router)   # Blood Glucose
app.include_router(bo.router)   # Oxygen Saturation (Blood Oxygen)
app.include_router(hr.router)   # Heart Rate
app.include_router(ss.router)   # Sleep
app.include_router(sd.router)   # Step
app.include_router(rr.router)   # Respiratory Rate
app.include_router(hrv.router)  # HRV
app.include_router(mv.router)   # Movement



from typing import Union
from fastapi import FastAPI
from app.routers import st, bp, bg, bo, hr, ss, sd

app = FastAPI()

# 기본 엔드포인트
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# 각 데이터 타입별 라우터 등록
app.include_router(st.router)
app.include_router(bp.router)
app.include_router(bg.router)
app.include_router(bo.router)
app.include_router(hr.router)
app.include_router(ss.router)
app.include_router(sd.router)



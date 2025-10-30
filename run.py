"""
Samsung Health Data API Server
서버 실행 스크립트
"""
import uvicorn
import os
from dotenv import load_dotenv

# 환경변수 로드
load_dotenv()

if __name__ == "__main__":
    # 환경변수에서 설정 읽기
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "18000"))
    limit_request_size = int(os.getenv("UVICORN_LIMIT_REQUEST_SIZE", "104857600"))  # 100MB
    
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True,
        limit_max_requests=10000,
        timeout_keep_alive=300,
        # 대용량 요청 처리를 위한 설정 (100MB)
        limit_concurrency=1000,
        backlog=2048
    )

import json
import os
from datetime import datetime

def save_data(data):
    # 저장 디렉토리 생성
    save_dir = "/workspace/8889/data"
    os.makedirs(save_dir, exist_ok=True)

    # 파일명: 데이터 타입_타임스탬프.json
    data_type = getattr(data, "DATA_TYPE", "unknown")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S%f") 
    filename = f"{data_type}_{timestamp}.json"
    filepath = os.path.join(save_dir, filename)

    # Pydantic 모델을 dict로 변환
    data_dict = data.dict()
    
    # DATA_LIST가 문자열로 전송된 경우 JSON 파싱 처리
    # 안드로이드 앱에서 DATA_LIST를 JSON 문자열로 전송할 수 있음
    if "DATA_LIST" in data_dict and isinstance(data_dict["DATA_LIST"], str):
        try:
            data_dict["DATA_LIST"] = json.loads(data_dict["DATA_LIST"])
        except json.JSONDecodeError:
            # 이미 파싱된 데이터거나 올바른 형식이 아닌 경우 그대로 사용
            pass
    
    # 데이터 저장
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data_dict, f, ensure_ascii=False, indent=2)

    return {"result": "success", "filepath": filepath}
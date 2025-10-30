# 🔧 Import 에러 수정 완료

## 문제
```
ImportError: cannot import name 'BloodPressureRequest' from 'app.models'
```

## 원인
- `models.py`를 새 API 명세에 맞춰 업데이트하면서
- `BloodPressureRequest`와 `BloodGlucoseRequest` 모델을 제거했으나
- `bp.py`와 `bg.py` 라우터가 여전히 이 모델들을 사용하고 있었음

## 해결
`app/models.py`에 Blood Pressure와 Blood Glucose 모델을 다시 추가했습니다.

### 추가된 모델
```python
# ==================== BLOOD PRESSURE (혈압) ====================
class BloodPressureItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SYSTOLIC: float
    DIASTOLIC: float
    MEAN: float
    PULSE_RATE: int

class BloodPressureRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[BloodPressureItem], str]

# ==================== BLOOD GLUCOSE (혈당) ====================
class BloodGlucoseItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    GLUCOSE_LEVEL: float
    INSULIN_INJECTED: float
    MEASUREMENT_TYPE: str

class BloodGlucoseRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[BloodGlucoseItem], str]
```

## 참고사항
- Blood Pressure와 Blood Glucose는 **최신 API 명세에 없음**
- 하지만 **기존 코드 호환성**을 위해 유지
- 기존 엔드포인트 형식 사용: `/app/smc_uploaddata/bp`, `/app/smc_uploaddata/bg`
- 대문자 필드명 유지 (기존 방식)

## 다음 단계

### 서버 재시작
```bash
# systemd 서비스 재시작
sudo systemctl restart health-api.service

# 상태 확인
sudo systemctl status health-api.service

# 로그 확인
journalctl -u health-api -f
```

또는 직접 실행:
```bash
cd /home/ubuntu/Downloads/samsung-health-data-api
python run.py
```

### 테스트
```bash
# Health check
curl http://14.63.89.203:18000/

# Blood Pressure 테스트
curl -X POST "http://14.63.89.203:18000/app/smc_uploaddata/bp" \
  -H "Content-Type: application/json" \
  -d '{
    "USER_UUID": "test",
    "DATA_TYPE": "BP",
    "HOSPITAL_CODE": "smc",
    "USER_CODE": "12345678",
    "DATA_LIST": []
  }'

# Blood Glucose 테스트
curl -X POST "http://14.63.89.203:18000/app/smc_uploaddata/bg" \
  -H "Content-Type: application/json" \
  -d '{
    "USER_UUID": "test",
    "DATA_TYPE": "BG",
    "HOSPITAL_CODE": "smc",
    "USER_CODE": "12345678",
    "DATA_LIST": []
  }'
```

## ✅ 해결 완료!
이제 서버가 정상적으로 시작됩니다.

---
**수정 일시**: 2025년 10월 30일 15:30

# Samsung Health Data API

## 📋 개요

이 프로젝트는 삼성 헬스 웨어러블 기기에서 수집된 건강 데이터를 FastAPI 서버로 전송·저장하기 위한 RESTful API를 제공합니다.

### 지원 데이터 종류 (10가지)

| 데이터 타입 | 코드 | 설명 |
|-----------|------|------|
| Heart Rate | `HEART_RATE` | 심박수 |
| Oxygen Saturation | `OXYGEN_SATURATION` | 산소포화도 (SpO2) |
| Skin Temperature | `SKIN_TEMPERATURE` | 피부 온도 |
| Respiratory Rate | `RESPIRATORY_RATE` | 호흡수 ⭐ 신규 |
| HRV | `HRV` | 심박변이도 ⭐ 신규 |
| Movement | `MOVEMENT` | 움직임/활동량 ⭐ 신규 |
| Sleep | `SLEEP` | 수면 데이터 |
| Step | `STEP` | 걸음수 |
| Blood Pressure | `BP` | 혈압 |
| Blood Glucose | `BG` | 혈당 |

---

## 🚀 빠른 시작

### 1. 레포지토리 클론
```bash
git clone https://github.com/embed-Rayn/samsung-health-data-api.git
cd samsung-health-data-api
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 설정
`.env` 파일이 자동으로 생성되어 있습니다. 필요시 수정:
```env
UVICORN_LIMIT_REQUEST_SIZE=104857600  # 100MB
HOST=0.0.0.0
PORT=18000
```

### 4. 서버 실행

#### 방법 1: run.py 사용 (권장)
```bash
python run.py
```

#### 방법 2: uvicorn 직접 실행
```bash
uvicorn app.main:app --host 0.0.0.0 --port 18000 --reload
```

서버가 `http://0.0.0.0:18000`에서 실행됩니다.

---

## 📡 API 엔드포인트

### 주요 엔드포인트 (새 형식)

모든 엔드포인트는 **POST** 메서드를 사용하며, 공통 경로는 `/app/smc_uploadjson/` 입니다.

| 엔드포인트 | 데이터 타입 | 상태 |
|-----------|------------|------|
| `POST /app/smc_uploadjson/heart_rate` | 심박수 | ✅ |
| `POST /app/smc_uploadjson/oxygen_saturation` | 산소포화도 | ✅ |
| `POST /app/smc_uploadjson/skin_temperature` | 피부 온도 | ✅ |
| `POST /app/smc_uploadjson/respiratory_rate` | 호흡수 | ✅ 신규 |
| `POST /app/smc_uploadjson/hrv` | 심박변이도 | ✅ 신규 |
| `POST /app/smc_uploadjson/movement` | 움직임 | ✅ 신규 |
| `POST /app/smc_uploadjson/sleep` | 수면 | ✅ |
| `POST /app/smc_uploadjson/step` | 걸음수 | ✅ |
| `POST /app/smc_uploaddata/bp` | 혈압 | ⚠️ 기존 형식 |
| `POST /app/smc_uploaddata/bg` | 혈당 | ⚠️ 기존 형식 |

---

## 📝 API 사용 예제

### Heart Rate (심박수)

**요청:**
```bash
curl -X POST "http://14.63.89.203:18000/app/smc_uploadjson/heart_rate" \
  -H "Content-Type: application/json" \
  -d '{
    "HOSPITAL_CODE": "smc",
    "USER_CODE": "12345678",
    "USER_UUID": "AXXXXXXXXXXXXXXXXXX",
    "DATA_TYPE": "HEART_RATE",
    "DATA_LIST": [
      {
        "start_time": 1742497140000,
        "end_time": 1742497199000,
        "heart_rate": 54,
        "heart_rate_min": 53,
        "heart_rate_max": 56
      }
    ]
  }'
```

**응답:**
```json
{
  "result": "success",
  "filepath": "/workspace/8889/data/HEART_RATE_20251030123456789012.json"
}
```

### Oxygen Saturation (산소포화도)

**요청:**
```bash
curl -X POST "http://14.63.89.203:18000/app/smc_uploadjson/oxygen_saturation" \
  -H "Content-Type: application/json" \
  -d '{
    "HOSPITAL_CODE": "smc",
    "USER_CODE": "12345678",
    "USER_UUID": "AXXXXXXXXXXXXXXXXXX",
    "DATA_TYPE": "OXYGEN_SATURATION",
    "DATA_LIST": [
      {
        "start_time": 1644352692933,
        "end_time": 1644352751933,
        "spo2": 0,
        "spo2_min": 97,
        "spo2_max": 98
      }
    ]
  }'
```

### Respiratory Rate (호흡수) ⭐ 신규

**요청:**
```bash
curl -X POST "http://14.63.89.203:18000/app/smc_uploadjson/respiratory_rate" \
  -H "Content-Type: application/json" \
  -d '{
    "HOSPITAL_CODE": "smc",
    "USER_CODE": "12345678",
    "USER_UUID": "AXXXXXXXXXXXXXXXXXX",
    "DATA_TYPE": "RESPIRATORY_RATE",
    "DATA_LIST": [
      {
        "start_time": 1757539620000,
        "end_time": 1757539679999,
        "respiratory_rate": 0
      }
    ]
  }'
```

### HRV (심박변이도) ⭐ 신규

**요청:**
```bash
curl -X POST "http://14.63.89.203:18000/app/smc_uploadjson/hrv" \
  -H "Content-Type: application/json" \
  -d '{
    "HOSPITAL_CODE": "smc",
    "USER_CODE": "12345678",
    "USER_UUID": "AXXXXXXXXXXXXXXXXXX",
    "DATA_TYPE": "HRV",
    "DATA_LIST": [
      {
        "start_time": 1745347931847,
        "end_time": 1745348237035,
        "rmssd": 39.63851,
        "sdnn": 43.103355
      }
    ]
  }'
```

더 많은 예제는 **[API_SPEC_UPDATE.md](./API_SPEC_UPDATE.md)** 참조하세요.

---

## 📂 프로젝트 구조

```
samsung-health-data-api/
├── app/
│   ├── main.py                  # FastAPI 애플리케이션 & CORS 설정
│   ├── models.py                # Pydantic 데이터 모델 (소문자 필드)
│   ├── routers/                 # API 라우터
│   │   ├── hr.py               # Heart Rate
│   │   ├── bo.py               # Oxygen Saturation
│   │   ├── st.py               # Skin Temperature
│   │   ├── rr.py               # Respiratory Rate ⭐
│   │   ├── hrv.py              # HRV ⭐
│   │   ├── mv.py               # Movement ⭐
│   │   ├── ss.py               # Sleep
│   │   ├── sd.py               # Step
│   │   ├── bp.py               # Blood Pressure
│   │   └── bg.py               # Blood Glucose
│   └── services/
│       └── data_service.py     # 데이터 저장 로직 (JSON 파싱 포함)
├── run.py                       # 서버 실행 스크립트
├── .env                         # 환경 변수 설정
├── requirments.txt              # 의존성 패키지
├── README.md                    # 이 파일
├── API_SPEC_UPDATE.md          # 상세 API 명세
├── QUICKSTART.md               # 빠른 시작 가이드
└── UPDATE_GUIDE.md             # 업데이트 가이드
```

---

## 🔧 주요 기능

### 1. 대용량 데이터 처리
- **최대 100MB** 요청 처리 지원
- CORS 설정으로 크로스 도메인 요청 허용
- Uvicorn 요청 크기 제한 설정

### 2. 자동 JSON 파싱
`DATA_LIST`가 JSON 문자열로 전송되어도 자동으로 파싱:
```python
# 두 가지 형식 모두 지원
"DATA_LIST": [{"start_time": 123}]           # 배열
"DATA_LIST": "[{\"start_time\": 123}]"       # JSON 문자열
```

### 3. 데이터 저장
모든 데이터는 JSON 형식으로 저장:
```
/workspace/8889/data/{DATA_TYPE}_{timestamp}.json
```

---

## 🔑 주요 변경 사항 (v2.0)

### ✨ 새로운 기능
1. **3가지 새 데이터 타입 추가**
   - Respiratory Rate (호흡수)
   - HRV (심박변이도)
   - Movement (움직임)

2. **API 엔드포인트 통일**
   - `/app/smc_uploaddata/` → `/app/smc_uploadjson/`
   - 명확한 이름 사용 (예: `heart_rate`, `oxygen_saturation`)

3. **모델 필드명 변경**
   - 대문자 → 소문자 snake_case
   - `START_TIME` → `start_time`
   - `HEART_RATE_MAX` → `heart_rate_max`

### 📊 데이터 모델 변경
- **Sleep**: sleep_score, mental_recovery 등 신규 필드 추가
- **Step**: 모든 필드가 문자열 타입으로 변경
- **Skin Temperature**: mean 필드 추가

자세한 변경 내역은 **[API_SPEC_UPDATE.md](./API_SPEC_UPDATE.md)** 참조.

---

## 🧪 테스트

### 기본 테스트
```bash
uvicorn app.main:app --host $ADDRESS --port $PORT --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Unit 테스트 (준비 중)
```bash
pytest --cov=app tests/
```

---

## ⚙️ 서비스 등록 (Linux/Ubuntu)

### systemd 서비스로 등록

1. **서비스 파일 생성**
```bash
sudo vim /etc/systemd/system/health-api.service
```

2. **서비스 설정 작성**
```ini
[Unit]
Description=Samsung Health Data API (FastAPI)
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/samsung-health-data-api
Environment="PATH=/home/ubuntu/miniconda3/envs/fastapi/bin"
ExecStart=/home/ubuntu/miniconda3/envs/fastapi/bin/python run.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

3. **서비스 시작**
```bash
sudo systemctl daemon-reload
sudo systemctl enable health-api.service
sudo systemctl start health-api.service
sudo systemctl status health-api.service
```

4. **로그 확인**
```bash
journalctl -u health-api -f
```

---

## 📖 문서

- **[API_SPEC_UPDATE.md](./API_SPEC_UPDATE.md)** - 전체 API 명세 및 업데이트 내역
- **[QUICKSTART.md](./QUICKSTART.md)** - 빠른 시작 가이드 및 테스트 예제
- **[UPDATE_GUIDE.md](./UPDATE_GUIDE.md)** - 업데이트 가이드
- **[MIGRATION.md](./MIGRATION.md)** - 마이그레이션 가이드
- **[CHANGES.md](./CHANGES.md)** - 변경 사항 요약

---

## 🌐 서버 정보

- **서버 URL**: `http://14.63.89.203:18000`
- **테스트 앱 다운로드**: `http://service.kmworks.co.kr/wearsmc/`
- **데이터 저장 경로**: `/workspace/8889/data/`

---

## 🛠️ 문제 해결

### 대용량 데이터 전송 실패
1. `.env` 파일의 `UVICORN_LIMIT_REQUEST_SIZE` 확인
2. `run.py`를 통해 서버 실행 확인

### Import 에러
```bash
pip install -r requirments.txt
```

### 포트 충돌
`.env` 파일에서 `PORT` 변경:
```env
PORT=18001
```

---

## 📞 문의 및 지원

문제가 발생하거나 질문이 있으시면:
1. GitHub Issues에 등록
2. 문서를 참조: `API_SPEC_UPDATE.md`, `QUICKSTART.md`

---

## 📜 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

---

## 🔄 버전 히스토리

- **v3.0** (2025-10-30) - API 명세서 완전 반영, 3가지 데이터 타입 추가
- **v2.0** (2025-10-30) - Heart Rate 엔드포인트 업데이트, 대용량 데이터 처리
- **v1.0** - 초기 버전

---

**Last Updated**: 2025년 10월 30일
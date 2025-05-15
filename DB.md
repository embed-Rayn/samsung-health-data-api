# DDL
```SQL
-- Skin Temperature
CREATE TABLE skin_temperature (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    temperature FLOAT,
    min FLOAT,
    max FLOAT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);

-- Blood Pressure
CREATE TABLE blood_pressure (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    systolic FLOAT,
    diastolic FLOAT,
    mean FLOAT,
    pulse_rate INT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);

-- Blood Glucose
CREATE TABLE blood_glucose (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    glucose_level FLOAT,
    insulin_injected FLOAT,
    measurement_type VARCHAR(32),
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);

-- Blood Oxygen
CREATE TABLE blood_oxygen (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    spo2 FLOAT,
    min FLOAT,
    max FLOAT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);

-- Heart Rate
CREATE TABLE heart_rate (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    heart_rate FLOAT,
    min FLOAT,
    max FLOAT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);

-- Sleep Session
CREATE TABLE sleep_session (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    sleep_seconds INT,
    awake_seconds INT,
    rem_seconds INT,
    light_seconds INT,
    deep_seconds INT,
    unknown_seconds INT,
    max_oxygen INT,
    min_oxygen INT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);

-- Step Daily
CREATE TABLE step_daily (
    id SERIAL PRIMARY KEY,
    user_uuid VARCHAR(64) NOT NULL,
    data_uuid VARCHAR(64) NOT NULL,
    day_time BIGINT NOT NULL,
    start_time BIGINT NOT NULL,
    end_time BIGINT NOT NULL,
    time_offset BIGINT NOT NULL,
    steps INT,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE (user_uuid, data_uuid)
);
```


# PostgreSQL 설치 및 기본 설정 가이드 (Windows 기준)

## 1. PostgreSQL 다운로드 및 설치

1. [공식 다운로드 페이지](https://www.postgresql.org/download/windows/)에서 Windows용 인스톨러 다운로드
2. 다운로드한 인스톨러 실행
3. 설치 경로, 데이터 디렉토리, 비밀번호(꼭 기억!), 포트(기본 5432) 등 설정
4. Stack Builder는 선택 사항(필요 없으면 체크 해제)
5. 설치 완료 후 마침

## 2. 환경 변수 설정 (선택)

- `C:\Program Files\PostgreSQL\16\bin` (버전에 따라 다름)을 시스템 PATH에 추가하면 어디서든 psql 등 명령어 사용 가능

## 3. PostgreSQL 서비스 시작/중지

- 설치 시 자동으로 서비스가 실행됨
- 서비스 관리:  
  `services.msc` → PostgreSQL 서비스에서 시작/중지 가능

## 4. pgAdmin 접속

- 설치된 pgAdmin 실행
- 서버 추가 → 비밀번호 입력 → 접속

## 5. 명령줄에서 접속

```bash
psql -U postgres
```
- 비밀번호 입력

## 6. 데이터베이스 및 사용자 생성

```sql
-- 데이터베이스 생성
CREATE DATABASE healthdb;

-- 사용자 생성 (예시)
CREATE USER healthuser WITH PASSWORD 'yourpassword';

-- 권한 부여
GRANT ALL PRIVILEGES ON DATABASE healthdb TO healthuser;
```

## 7. 테이블 생성

- 위에서 안내한 DDL을 pgAdmin 쿼리 툴 또는 psql에서 실행

## 8. 외부 접속 허용 (필요시)

- `C:\Program Files\PostgreSQL\16\data\postgresql.conf`  
  `listen_addresses = '*'` 로 수정

- `C:\Program Files\PostgreSQL\16\data\pg_hba.conf`  
  아래 내용 추가 (예시, 보안에 유의)
  ```
  host    all             all             0.0.0.0/0               md5
  ```

- 서비스 재시작 필요

## 9. 방화벽 예외 추가

- Windows 방화벽에서 5432 포트 인바운드 허용

---

## 참고

- 공식 문서: https://www.postgresql.org/docs/
- pgAdmin: https://www.pgadmin.org/
- 설치 후 반드시 비밀번호, 포트, 외부접속 보안 등 확인

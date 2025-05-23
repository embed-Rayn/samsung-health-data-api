from pydantic import BaseModel
from typing import List

class SkinTemperatureItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    TEMPERATURE: float
    MIN: float
    MAX: float

class SkinTemperatureRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[SkinTemperatureItem]

class BloodPressureItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
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
    DATA_LIST: List[BloodPressureItem]

class BloodGlucoseItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    GLUCOSE_LEVEL: float
    INSULIN_INJECTED: float
    MEASUREMENT_TYPE: str

class BloodGlucoseRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodGlucoseItem]

class BloodOxygenItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SPO2: float
    MIN: float
    MAX: float

class BloodOxygenRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodOxygenItem]

class HeartRateItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    HEART_RATE: float
    MIN: float
    MAX: float

class HeartRateRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[HeartRateItem]

class SleepSessionItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SLEEP_SECONDS: int
    AWAKE_SECONDS: int
    REM_SECONDS: int
    LIGHT_SECONDS: int
    DEEP_SECONDS: int
    UNKNOWN_SECONDS: int
    MAX_OXYGEN: int
    MIN_OXYGEN: int

class SleepSessionRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[SleepSessionItem]

class StepDailyItem(BaseModel):
    DATA_UUID: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DAY_TIME: int
    COUNT: int
    CALORIE: float
    CALORIE: float
    SPEED: float

class StepDailyRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[StepDailyItem]
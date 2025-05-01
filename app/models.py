from pydantic import BaseModel
from typing import List, Optional

class SkinTemperatureItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    TIME_OFFSET: int
    MEAN: float

class SkinTemperatureRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[SkinTemperatureItem]

class BloodPressureItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SYSTOLIC: float
    DIASTOLIC: float
    MEAN: int
    PULSE_RATE: int

class BloodPressureRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodPressureItem]

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
    DATA_LIST: List[BloodGlucoseItem]

class BloodOxygenItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SPO2: float
    HEART_RATE: float
    MIN: float
    MAX: float

class BloodOxygenRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodOxygenItem]

class HeartRateItem(BaseModel):
    DATA_UUID: str
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
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    STEPS: int
    DISTANCE: Optional[float] = None
    CALORIES: Optional[float] = None

class StepDailyRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[StepDailyItem]
from pydantic import BaseModel
from typing import List, Optional

class SkinTemperatureItem(BaseModel):
    DATA_UUID: str
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
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SYSTOLIC: int
    DIASTOLIC: int
    PULSE: int

class BloodPressureRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodPressureItem]

class BloodGlucoseItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    GLUCOSE: float

class BloodGlucoseRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodGlucoseItem]

class BloodOxygenItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    OXYGEN: float

class BloodOxygenRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[BloodOxygenItem]

class HeartRateItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    HEART_RATE: int

class HeartRateRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    DATA_LIST: List[HeartRateItem]

class SleepSessionItem(BaseModel):
    DATA_UUID: str
    START_TIME: int
    END_TIME: int
    TIME_OFFSET: int
    SLEEP_STAGE: Optional[str] = None
    DURATION: int

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
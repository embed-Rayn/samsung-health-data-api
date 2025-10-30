from pydantic import BaseModel
from typing import List, Optional, Union

# ==================== OXYGEN SATURATION (산소포화도) ====================
class OxygenSaturationItem(BaseModel):
    start_time: int
    end_time: int
    spo2: float
    spo2_min: float
    spo2_max: float

class OxygenSaturationRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[OxygenSaturationItem], str]  # JSON 문자열도 허용

# ==================== SKIN TEMPERATURE (피부 온도) ====================
class SkinTemperatureItem(BaseModel):
    start_time: int
    end_time: int
    min: float
    max: float
    mean: float

class SkinTemperatureRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[SkinTemperatureItem], str]

# ==================== HEART RATE (심박수) ====================
class HeartRateItem(BaseModel):
    start_time: int
    end_time: int
    heart_rate: float
    heart_rate_min: float
    heart_rate_max: float

class HeartRateRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[HeartRateItem], str]

# ==================== RESPIRATORY RATE (호흡수) ====================
class RespiratoryRateItem(BaseModel):
    start_time: int
    end_time: int
    respiratory_rate: float

class RespiratoryRateRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[RespiratoryRateItem], str]

# ==================== HRV (심박변이도) ====================
class HRVItem(BaseModel):
    start_time: int
    end_time: int
    rmssd: float
    sdnn: float

class HRVRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[HRVItem], str]

# ==================== MOVEMENT (움직임) ====================
class MovementItem(BaseModel):
    start_time: int
    end_time: int
    activity_level: int

class MovementRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[MovementItem], str]

# ==================== SLEEP (수면) ====================
class SleepItem(BaseModel):
    start_time: int
    end_time: int
    sleep_score: str
    sleep_duration: str
    mental_recovery: str
    physical_recovery: str
    movement_awakening: str
    total_light_duration: Optional[str] = ""
    total_rem_duration: Optional[str] = ""

class SleepRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[SleepItem], str]

# ==================== STEP (걸음수) ====================
class StepItem(BaseModel):
    daytime: str
    count: str
    calorie: str
    distance: str
    speed: str

class StepRequest(BaseModel):
    USER_UUID: str
    DATA_TYPE: str
    HOSPITAL_CODE: str
    USER_CODE: str
    DATA_LIST: Union[List[StepItem], str]

# ==================== BLOOD PRESSURE (혈압) ====================
# 명세서에 없지만 기존 코드 호환성을 위해 유지
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
# 명세서에 없지만 기존 코드 호환성을 위해 유지
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

# ==================== 하위 호환성을 위한 별칭 ====================
# 기존 코드와의 호환성을 위해 유지
BloodOxygenItem = OxygenSaturationItem
BloodOxygenRequest = OxygenSaturationRequest
SleepSessionItem = SleepItem
SleepSessionRequest = SleepRequest
StepDailyItem = StepItem
StepDailyRequest = StepRequest
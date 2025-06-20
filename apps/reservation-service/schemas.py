from pydantic import BaseModel
from datetime import date, time
from enum import Enum
from typing import Optional

class ReservationStatusEnum(str, Enum):
    PENDING = "대기"
    CONFIRMED = "확정"
    CANCELED = "취소"

class ReservationCreate(BaseModel):
    content_id: int
    date: date
    time: Optional[time]
    people: int

class ReservationOut(ReservationCreate):
    id: int
    user_id: int
    status: ReservationStatusEnum

    model_config = {
        "from_attributes": True 
    }

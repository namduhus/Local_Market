from sqlalchemy import Column, Integer, Date, Time, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum as PyEnum

class ReservationStatus(PyEnum):
    PENDING = "대기"
    CONFIRMED = "확정"
    CANCELED = "취소"

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(Integer, nullable=False)  # 콘텐츠 ID
    user_id = Column(Integer, nullable=False)     # 예약자 ID
    date = Column(Date, nullable=False)           # 예약 일자
    time = Column(Time, nullable=True)            # (선택) 시간
    people = Column(Integer, default=1)           # 인원 수
    status = Column(Enum(ReservationStatus), default=ReservationStatus.PENDING)
    is_active = Column(Boolean, default=True)

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Reservation, ReservationStatus
from schemas import ReservationCreate, ReservationOut
from utils.jwt_handler import get_current_user
from crud import create_reservation, get_user_reservations, cancel_reservation

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post(path="/", summary="콘텐츠예약 생성 기능", description="에약을 생성하는 기능입니다.",tags=["Create"],response_model=ReservationOut)
def create_new_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return create_reservation(db=db, reservation=reservation, user_id=current_user)

@router.get("/my", summary="내 예약 조회 기능", description="내 생성된 예약 조회 기능입니다.",tags=["Search"],response_model=list[ReservationOut])
def read_my_reservations(
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user),
):
    return get_user_reservations(db, user_id=current_user)

@router.patch("/{id}/cancel", summary="예약 취소 기능", description="예약 취소 기능입니다.",tags=["Cancel"],response_model=ReservationOut)
def cancel_my_reservation(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return cancel_reservation(db=db, reservation_id=id, user_id=current_user)
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Reservation, ReservationStatus
from schemas import ReservationCreate, ReservationOut
from utils.jwt_handler import get_current_user
from crud import create_reservation  # 아래에 만들 예정

router = APIRouter(prefix="/reservations", tags=["Reservations"])

@router.post("/", response_model=ReservationOut)
def create_new_reservation(
    reservation: ReservationCreate,
    db: Session = Depends(get_db),
    current_user: int = Depends(get_current_user)
):
    return create_reservation(db=db, reservation=reservation, user_id=current_user)

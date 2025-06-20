from sqlalchemy.orm import Session
from models import Reservation, ReservationStatus
from schemas import ReservationCreate
from datetime import datetime

def create_reservation(db: Session, reservation: ReservationCreate, user_id: int):
    db_reservation = Reservation(
        content_id=reservation.content_id,
        user_id=user_id,
        date=reservation.date,
        time=reservation.time,
        people=reservation.people,
        status=ReservationStatus.PENDING,
        is_active=True
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_user_reservations(db: Session, user_id: int):
    return db.query(Reservation).filter(Reservation.user_id == user_id).order_by(Reservation.date.desc()).all()
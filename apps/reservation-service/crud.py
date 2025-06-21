from sqlalchemy.orm import Session
from models import Reservation, ReservationStatus
from schemas import ReservationCreate
from datetime import datetime
from fastapi import HTTPException, status

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

def cancel_reservation(db: Session, reservation_id: int, user_id: int) -> Reservation:
    reservation = db.query(Reservation).filter(Reservation.id == reservation_id).first()

    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    print(f"[DEBUG] user_id: {user_id} ({type(user_id)}), reservation.user_id: {reservation.user_id} ({type(reservation.user_id)})")

    if int(reservation.user_id) != int(user_id):
        raise HTTPException(status_code=403, detail="Not your reservation")

    if reservation.status != ReservationStatus.PENDING:
        raise HTTPException(status_code=400, detail="Only pending reservations can be canceled")

    reservation.status = ReservationStatus.CANCELED
    db.commit()
    db.refresh(reservation)
    return reservation
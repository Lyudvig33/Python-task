from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from datetime import datetime,timedelta
from sqlalchemy import func


def is_table_available(db: Session, table_id: int, start_time: datetime, duration_minutes: int) -> bool:
    end_time = start_time + timedelta(minutes=duration_minutes)

    try:
        reservations = db.query(Reservation).filter(
            Reservation.table_id == table_id
        ).all()

    
        for res in reservations:
            res_end = res.reservation_time + timedelta(minutes=res.duration_minutes)
            if res.reservation_time < end_time and res_end > start_time:
                return False

        return True
    

    except Exception as e:
        print("Error in is_table_available:", e)
    return False 
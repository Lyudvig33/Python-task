from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas.reservation import ReservationCreate,ReservationRead
from app.models.reservation import Reservation
from app.db.session import SessionLocal
from app.services.reservation_service import is_table_available

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/',response_model=list[ReservationRead])
def get_reservation(db: Session = Depends(get_db)):
    return db.query(Reservation).all()


@router.post('/',response_model=ReservationRead)
def create_reservation(reservation: ReservationCreate,db: Session = Depends(get_db)):
    try:
        if not is_table_available(db, reservation.table_id,reservation.reservation_time,reservation.duration_minutes):
            raise HTTPException(status_code=400,detail=f'Table is already reserved for this time slot: {reservation.duration_minutes} minutes')
        
        db_reservation = Reservation(**reservation.model_dump())
        db.add(db_reservation)
        db.commit()
        db.refresh(db_reservation)
        return db_reservation

    except HTTPException:
            raise  
    except Exception as e:
        print("Unexpected error in create_reservation:", e)
    raise HTTPException(status_code=500, detail="Internal Server Error")


@router.delete('/{reservation_id}')
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    res = db.query(Reservation).get(reservation_id)
    if not res:
        raise HTTPException(status_code=404,detail='Reservation not found')
    
    db.delete(res)
    db.commit()
    return {'Detail': "Reservation deleted"}
    

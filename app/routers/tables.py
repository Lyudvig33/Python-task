from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.schemas.table import TableCreate, TableRead
from app.models.table import Table
from app.db.session import SessionLocal
from app.models.reservation import Reservation


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/',response_model=list[TableRead])
def get_tables(db: Session = Depends(get_db)):
    return db.query(Table).all()


@router.post('/',response_model=TableRead)
def create_table(table: TableCreate, db: Session = Depends(get_db)):
    db_table = Table(**table.model_dump())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete('/{table_id}')
def delete_table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(Table).filter(Table.id == table_id).first()
    if not table:
        raise HTTPException(status_code=404, detail='table not found')
    
    db.query(Reservation).filter(Reservation.table_id == table_id).delete()
    db.delete(table)
    db.commit()
    return {'detail': 'Table deleted'}

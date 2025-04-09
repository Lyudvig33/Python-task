from fastapi import FastAPI
from app.routers import tables, reservations
from app.db.session import engine
from app.db.base import Base

app = FastAPI(title="Restaurant Booking API")

Base.metadata.create_all(bind=engine)

app.include_router(tables.router, prefix="/tables", tags=["Tables"])
app.include_router(reservations.router, prefix="/reservations", tags=["Reservations"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
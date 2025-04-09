from sqlalchemy import Column, Integer,String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.db.base import Base

class Reservation(Base):
    __tablename__ = "reservation"

    id = Column(Integer,primary_key=True,index=True)
    customer_name = Column(String,nullable=False)
    table_id = Column(Integer, ForeignKey("tables.id", ondelete="CASCADE"), nullable=False)
    reservation_time = Column(DateTime,nullable=False)
    duration_minutes = Column(Integer,nullable=False)

    table = relationship("Table",backref='reservation',passive_deletes=True)
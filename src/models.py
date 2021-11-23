from sqlalchemy import Column, Integer, String, Date

from database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    representative = Column(String)
    contract_start = Column(Date)
    Country = Column(String)

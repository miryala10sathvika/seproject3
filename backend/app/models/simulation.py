from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Simulation(Base):
    __tablename__ = "simulations"
    id = Column(Integer, primary_key=True, index=True)
    scenario_type = Column(String)
    result = Column(String)

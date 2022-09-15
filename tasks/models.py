from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from geoalchemy2 import Geometry
from .database import Base


class Countries(Base):
    __tablename__ = "corrected_countries"

    id = Column(Integer, primary_key=True, index=True)
    geom = Column(Geometry('POLYGON'))
    ADMIN = Column(String)
    ISO_A3 = Column(String)


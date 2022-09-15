from typing import List, Union
from geoalchemy2 import Geometry
from pydantic import BaseModel



class countryname(BaseModel):
    id: int
    geom: Geometry
    ADMIN: str
    ISO_A3:str
    class Config:
        orm_mode = True

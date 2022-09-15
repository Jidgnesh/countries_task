from typing import Union
import json
import pickle

from fastapi import FastAPI



from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}
    
@app.get("/jidgnesh")
def read_my_name():
    return {"name":"jidgnesh"}

@app.get("/c")
def getdata():
    file = open("countries.geojson")
    #return json.load(file)
    data_count = json.load(file)
    #return data_count
    
    feature_list = data_count["features"]
    
    for i in feature_list:
        if i["geometry"]["type"] == "Polygon":
            i["geometry"]["type"] = "MultiPolygon"
    
    with open("corrected_countries.geojson", "w") as outfile:
           json.dump(data_count,outfile)
 
    return data_count

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/items/", response_model=schemas.countryname)
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


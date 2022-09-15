from sqlalchemy.orm import Session

from . import models, schemas



def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Countries).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.countryname, user_id: int):
    db_item = models.Countries(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

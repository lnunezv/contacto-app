from sqlalchemy.orm import Session
from . import models, schemas


def create_contact(db: Session, contact: schemas.ContactCreate):
    db_contact = models.Contact(**contact.model_dump())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(db: Session):
    return db.query(models.Contact).all()

def delete_contact(db: Session, contact_id: int):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()
    
    if not contact:
        return None

    db.delete(contact)
    db.commit()
    return contact

def update_contact(db: Session, contact_id: int, contact_data: schemas.ContactCreate):
    contact = db.query(models.Contact).filter(models.Contact.id == contact_id).first()

    if not contact:
        return None

    contact.name = contact_data.name
    contact.email = contact_data.email
    contact.subject = contact_data.subject
    contact.message = contact_data.message

    db.commit()
    db.refresh(contact)
    return contact
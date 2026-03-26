from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, SessionLocal
from . import models, schemas, crud
from .mailer import send_contact_email
from fastapi.middleware.cors import CORSMiddleware

# CREA LAS TABLAS
Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DEPENDENCIA DE DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "API funcionando"}


# CREAR CONTACTO
@app.post("/contacts", response_model=schemas.ContactResponse)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    
    new_contact = crud.create_contact(db, contact)

    # ENVÍA CORREO
    try:
        send_contact_email(
            name=contact.name,
            email=contact.email,
            subject=contact.subject,
            message=contact.message
        )
    except Exception as e:
        print("Error enviando correo:", e)

    return new_contact


# LISTAR CONTACTOS
@app.get("/contacts", response_model=list[schemas.ContactResponse])
def get_contacts(db: Session = Depends(get_db)):
    return crud.get_contacts(db)



from fastapi import HTTPException
@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_contact(db, contact_id)
    
    if not deleted:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")
    
    return {"message": "Contacto eliminado"}


@app.put("/contacts/{contact_id}", response_model=schemas.ContactResponse)
def update_contact(contact_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    
    updated = crud.update_contact(db, contact_id, contact)

    if not updated:
        raise HTTPException(status_code=404, detail="Contacto no encontrado")

    return updated
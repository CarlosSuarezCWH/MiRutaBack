from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session, sessionmaker
from config.database import conn, engine
from routes.ticket_routes import get_ticket
import qrcode

app = FastAPI()
router = APIRouter()

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/generate-qr/{ticket_id}")
async def generate_qr(ticket_id: int):
    ticket = get_ticket(ticket_id, db=Depends(get_db))
    return ticket
    #qr = qrcode.QRCode(
    #    version=1,
    #    error_correction=qrcode.constants.ERROR_CORRECT_L,
    #    box_size=10,
    #    border=4,
    #)
    #qr.add_data(ticket)
    #qr.make(fit=True)
    #img = qr.make_image(fill_color="black", back_color="white")
    #img.save(f"resources/images_qr/ticket_{ticket_id}.png")
    #return {"message": "QR code generated successfully"}

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import qrcode
from io import BytesIO
from fastapi.responses import StreamingResponse
from typing import Optional
from datetime import date
from schemas.TicketSchema import TicketResponseSchema

app = FastAPI()

@app.post("/generate_qr/", response_class=StreamingResponse)
async def generate_qr(ticket: TicketResponseSchema):
    # Convertir los datos del ticket en una cadena para generar el QR
    ticket_data_str = str(ticket.json())

    # Crear un objeto BytesIO para almacenar el QR generado
    qr_image_stream = BytesIO()

    # Generar el código QR
    qr = qrcode.make(ticket_data_str)

    # Guardar el código QR en el objeto BytesIO
    qr.save(qr_image_stream, format="PNG")

    # Convertir el objeto BytesIO a una respuesta de transmisión
    qr_image_stream.seek(0)
    return qr_image_stream
# google_wallet_api.py

from fastapi import FastAPI
from .google_wallet import GoogleWalletService

app = FastAPI()
google_wallet_service = GoogleWalletService('path_to_service_account_json')

@app.post("/send-to-google-wallet/")
async def send_to_google_wallet(ticket_data: dict):
    # Utilizar el servicio de la Wallet de Google para enviar el boleto
    google_pass_url = google_wallet_service.generate_ticket_pass(ticket_data)
    
    return {"google_pass_url": google_pass_url}

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routes.register import register_router
from routes.login import login_router
from routes.terminales import terminal_router

app = FastAPI()

# Configura CORS
origins = [
    "*",  # Permite peticiones desde la app Flutter
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejar solicitudes OPTIONS explícitamente para todos los endpoints
@app.options("/{path:path}")
async def options_handler(path: str):
    return {"detail": "Allowed"}

app.include_router(register_router, prefix="/api/v1")
app.include_router(login_router, prefix="/api/v1")
app.include_router(terminal_router, prefix="/api/v1")
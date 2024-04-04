from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.sessions import SessionMiddleware

# Importación de routers individuales
from routes import (
    bus_routes,
    permission_routes,
    profile_routes,
    role_routes,
    route_routes,
    terminal_routes,
    ticket_routes,
    ticket_type_routes,
    transaction_routes,
    user_routes,
    #qr_generation_api,
)

app = FastAPI()

# Configuración de CORS (ajuste los orígenes según sea necesario)
app.add_middleware(
    CORSMiddleware,
    # Reemplace con los orígenes permitidos
    #allow_origins=["http://localhost:8080"], # Permitir solo a http://localhost:8080
    allow_origins=["*"], # Permitir a todos los orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware de autenticación y sesión (opcional)
# Descomente y configure estos si es necesario
# app.add_middleware(AuthenticationMiddleware)
# app.add_middleware(SessionMiddleware, secret_key="your_secret_key")

# Manejar solicitudes OPTIONS explícitamente para todos los endpoints
@app.options("/{path:path}")
async def options_handler(path: str):
    return {"detail": "Allowed"}

# Registro de rutas con etiquetas descriptivas
app.include_router(user_routes.router, prefix="/api/v1", tags=["Gestión de Usuarios"])
app.include_router(transaction_routes.router, prefix="/api/v1", tags=["Transacciones"])
app.include_router(profile_routes.router, prefix="/api/v1", tags=["Perfiles de Usuario"])
app.include_router(ticket_routes.router, prefix="/api/v1", tags=["Boletos"])
app.include_router(ticket_type_routes.router, prefix="/api/v1", tags=["Tipos de Boleto"])
app.include_router(route_routes.router, prefix="/api/v1", tags=["Rutas"])
app.include_router(terminal_routes.router, prefix="/api/v1", tags=["Terminales"])
app.include_router(bus_routes.router, prefix="/api/v1", tags=["Autobuses"])
app.include_router(role_routes.router, prefix="/api/v1", tags=["Roles de Usuario"])
app.include_router(permission_routes.router, prefix="/api/v1", tags=["Permisos"])
#app.include_router(qr_generation_api.router, prefix="/api/v1", tags=["Generación de Códigos QR"])

# Manejo de errores (opcional: considere usar un manejador de excepciones global)

# ... su lógica de manejo de errores ...
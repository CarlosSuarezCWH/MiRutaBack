# Mi Ruta

Aplicacion basada en fastapi para generar el backend de la app basada en rutas de autobuses, tiempo de llegada y mas


## Instalación

1. Clona este repositorio.
2. Instala las dependencias con pip:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, utiliza el siguiente comando:

```bash
uvicorn app:app --reload --host 0.0.0.0
```

Este comando ejecutará la aplicación FastAPI y la hará accesible en `http://localhost:8000`.

## Endpoints

- `/api/v1/register`: Endpoint para registrar usuarios.
- `/api/v1/login`: Endpoint para iniciar sesión.
- `/api/v1/terminales`: Endpoint para trabajar con terminales.

## Contribuir

Si deseas contribuir a este proyecto, sigue los pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit de ellos (`git commit -am 'Agrega nueva funcionalidad'`).
4. Sube tus cambios a tu repositorio en GitHub (`git push origin feature/nueva-funcionalidad`).
5. Crea un pull request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia [MIT](https://opensource.org/licenses/MIT) - ver el archivo [LICENSE](LICENSE) para más detalles.

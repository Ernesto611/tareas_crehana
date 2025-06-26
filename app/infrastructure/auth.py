from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "super-secret"  # en producción, usar .env


@AuthJWT.load_config
def get_config():
    return Settings()

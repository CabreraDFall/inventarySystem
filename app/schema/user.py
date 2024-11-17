from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserBase(BaseModel):
    username: str = Field(..., description="Nombre de usuario único para el sistema", min_length=3, max_length=50)
    email: EmailStr = Field(..., description="Correo electrónico válido del usuario")
    full_name: Optional[str] = Field(None, description="Nombre completo del usuario, si está disponible", max_length=100)

class UserCreate(UserBase):
    password: str = Field(..., description="Contraseña del usuario, debe ser segura", min_length=8)

class User(UserBase):
    id: int = Field(..., description="Identificador único del usuario en el sistema")

    class Config:
        orm_mode = True

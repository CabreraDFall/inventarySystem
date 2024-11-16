from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class SupplierBase(BaseModel):
    name: str = Field(..., description="Nombre del proveedor", max_length=100)
    contact_name: Optional[str] = Field(None, description="Nombre del contacto principal del proveedor", max_length=100)
    phone_number: Optional[str] = Field(None, description="Número de teléfono del proveedor", regex=r"^\+?\d{1,15}$")
    email: Optional[EmailStr] = Field(None, description="Correo electrónico del proveedor")

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int = Field(..., description="Identificador único del proveedor")

    class Config:
        orm_mode = True

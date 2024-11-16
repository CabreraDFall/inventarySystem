from pydantic import BaseModel, Field
from typing import Optional

class ProductBase(BaseModel):
    name: str = Field(..., description="Nombre del producto", max_length=100)
    description: Optional[str] = Field(None, description="Descripción detallada del producto", max_length=500)
    price: float = Field(..., description="Precio del producto en unidades monetarias", gt=0)
    stock: int = Field(..., description="Cantidad de productos en stock", ge=0)

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int = Field(..., description="Identificador único del producto en el sistema")

    class Config:
        orm_mode = True

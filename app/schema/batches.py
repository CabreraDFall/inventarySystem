from pydantic import BaseModel, Field
from typing import Optional

class BatchBase(BaseModel):
    product_id: int = Field(..., description="Identificador del producto asociado al lote")
    quantity: int = Field(..., description="Cantidad de productos en el lote", gt=0)
    batch_code: str = Field(..., description="Código único del lote", max_length=50)
    expiration_date: Optional[str] = Field(None, description="Fecha de expiración del lote en formato YYYY-MM-DD")

class BatchCreate(BatchBase):
    pass

class Batch(BatchBase):
    id: int = Field(..., description="Identificador único del lote")

    class Config:
        orm_mode = True

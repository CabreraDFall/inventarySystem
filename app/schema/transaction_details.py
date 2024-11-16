from pydantic import BaseModel, Field
from typing import Optional

class TransactionDetailBase(BaseModel):
    transaction_id: int = Field(..., description="Identificador de la transacción a la que pertenece el detalle")
    product_id: int = Field(..., description="Identificador del producto involucrado en la transacción")
    quantity: int = Field(..., description="Cantidad de productos involucrados en la transacción", gt=0)
    price: float = Field(..., description="Precio unitario del producto en la transacción", gt=0)

class TransactionDetailCreate(TransactionDetailBase):
    pass

class TransactionDetail(TransactionDetailBase):
    id: int = Field(..., description="Identificador único del detalle de la transacción")

    class Config:
        orm_mode = True

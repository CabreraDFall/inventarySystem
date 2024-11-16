#Transactions.py


from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from transaction_details import TransactionDetailBase

class TransactionBase(BaseModel):
    transaction_type: str = Field(..., description="Tipo de transacción (por ejemplo: 'compra', 'venta')")
    total_amount: float = Field(..., description="Monto total de la transacción", gt=0)
    transaction_date: datetime = Field(..., description="Fecha y hora en que ocurrió la transacción")

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int = Field(..., description="Identificador único de la transacción")
    transaction_details: List[TransactionDetailBase] = Field(..., description="Detalles de los productos involucrados en la transacción")

    class Config:
        orm_mode = True

from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class StockHistoryBase(BaseModel):
    product_id: int = Field(..., description="Identificador del producto cuyo stock está siendo actualizado")
    quantity_changed: int = Field(..., description="Cantidad cambiada en el stock (puede ser positiva o negativa)", ge=-9999, le=9999)
    transaction_type: str = Field(..., description="Tipo de transacción (por ejemplo: 'entrada', 'salida')", max_length=50)
    change_date: datetime = Field(..., description="Fecha y hora del cambio de stock")

class StockHistoryCreate(StockHistoryBase):
    pass

class StockHistory(StockHistoryBase):
    id: int = Field(..., description="Identificador único del historial de existencias")

    class Config:
        orm_mode = True

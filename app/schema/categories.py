from pydantic import BaseModel, Field
from typing import Optional

class CategoryBase(BaseModel):
    name: str = Field(..., description="Nombre de la categoría", max_length=100)
    description: Optional[str] = Field(None, description="Descripción de la categoría", max_length=500)

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int = Field(..., description="Identificador único de la categoría")

    class Config:
        orm_mode = True

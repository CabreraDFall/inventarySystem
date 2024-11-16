from fastapi import APIRouter
from app import fake_data

router = APIRouter()


@router.get("/products" , tags=["Products"])
async def get_products():
    return fake_data["products"]
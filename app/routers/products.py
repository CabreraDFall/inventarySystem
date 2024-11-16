from fastapi import APIRouter

router = APIRouter()


@router.get("/products" , tags=["Products"])
async def get_products():
    return "products"
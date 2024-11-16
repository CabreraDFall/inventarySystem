from fastapi import APIRouter

router = APIRouter(prefix="/suppliers",tags=["Suppliers"])

@router.get("")
async def get_suppliers():
    return "suppliers"
from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("")
async def get_categories():
    return "get_categories"
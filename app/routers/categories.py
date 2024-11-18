from fastapi import APIRouter,HTTPException
from app import fake_data
from typing import List
from ..schema.categories import Category, CategoryCreate


router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=List[Category])
async def get_categories():
    category_with_id=[
        {**category, "id": idx+1} for idx, category in enumerate(fake_data["categories"])
    ]

    return category_with_id

@router.get("/{category_id}", response_model=Category)
def get_category_by_id(category_id: int):
    category_with_id = [
        {**category, "id": idx +1}for idx, category in enumerate(fake_data["categories"])
    ]

    category = next((category for category in category_with_id if category["id"]==category_id), None)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category

@router.post("/", response_model=Category)
def create_category(category: CategoryCreate):

    category_id = len(fake_data["categories"])+1

    new_category = category.dict()
    new_category["id"] = category_id

    fake_data["categories"].append(new_category)
    
    return new_category

@router.put("/{category_id}")
def update_category(category_id: int, category: CategoryCreate):
    category_with_id = [{**category, "id": idx+1} for idx, category in enumerate(fake_data["categories"])]

    existing_category = next((category for category in category_with_id if category["id"]==category_id), None)    

    if existing_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_category = {**existing_category, **category.dict()}

    for idx, category in enumerate(fake_data["categories"]):
        if category.get("id")== category_id:
            fake_data["categories"][idx] = update_category
            break

    return update_category

@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int):
    category_with_id = [
        {**category, "id": idx+1} for idx, category in enumerate(fake_data["categories"])
    ]
     
    category_index = next((idx for idx, category in enumerate(category_with_id) if category["id"]== category_id), None)

    if category_index is None:
        raise HTTPException(status_code=404, detail="User not Found")
    
    del fake_data["categories"][category_index]

    return None
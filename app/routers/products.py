from fastapi import APIRouter, HTTPException
from app import fake_data
from typing import List
from ..schema.products import Product, ProductCreate


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products():
    product_with_id=[
        {**product, "id": idx + 1} for idx, product in enumerate(fake_data["products"])
    ]
    return product_with_id


@router.get("/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    product_with_id = [
        {**products, "id": idx + 1} for idx, products in enumerate(fake_data["products"])
    ]

    product = next((product for product in product_with_id if product["id"] == product_id), None)

    if product is None:
        # Si el usuario no se encuentra, lanzar una excepción HTTP 404
        raise HTTPException(status_code=404, detail="User not found")
    
    return product

@router.post("/", response_model=Product)
def create_product(product:ProductCreate):
    product_id = len(fake_data["products"])+1

    new_product = product.dict()
    new_product["id"] = product_id

    fake_data["products"].append(new_product)

    return new_product

@router.put("/{product_id}")
def update_product(product_id:int, product: ProductCreate):
    product_with_id=[
        {**product, "id": idx+1} for idx, product in enumerate(fake_data["products"])
    ]

    exiting_product = next((product for product in product_with_id if product["id"]== product_id), None)

    if exiting_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    update_product= {**exiting_product, **product.dict()}

    for idx, product in enumerate(fake_data["products"]):
        if product.get("id") == product_id:
            fake_data["products"][idx] = update_product
            break

    return update_product

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id:int):
    product_with_id = [
        {**product, "id": idx +1} for idx, product in enumerate(fake_data["products"])
    ]

    product_index = next((idx for idx, product in enumerate(product_with_id) if product["id"]== product_id), None)

    if product_index is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    del fake_data["products"][product_index]

    return None
from fastapi import APIRouter, HTTPException
from app import fake_data
from typing import List
from ..schema.suppliers import Supplier, SupplierCreate
from ..utils.commons import create_list_with_id

router = APIRouter(prefix="/suppliers",tags=["Suppliers"])

@router.get("/", response_model=List[Supplier])
async def get_suppliers():
    return create_list_with_id("suppliers")
     

@router.get("/{supplier_id}", response_model=Supplier)
def get_supplier_by_id(supplier_id: int):
    supplier_with_id = create_list_with_id("suppliers")

    supplier = next((supplier for supplier in supplier_with_id if supplier["id"]==supplier_id), None)

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supllier not found")
    
    return supplier
    
@router.post("/")
def create_supplier(supplier: SupplierCreate):
    supplier_id = len(fake_data["suppliers"]) + 1

    new_supplier = supplier.dict()
    new_supplier["id"] = supplier_id

    fake_data["suppliers"].append(new_supplier)

    return new_supplier

@router.put("/{supplier_id}", response_model=Supplier )
def update_supplier(supplier_id: int, supplier: SupplierCreate):

    supplier_with_id = create_list_with_id("suppliers")

    existing_supplier = next((supplier for supplier in supplier_with_id if supplier["id"]== supplier_id), None)

    if existing_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    
    update_supplier = {**existing_supplier, **supplier.dict()}

    for idx, supplier in enumerate(fake_data["suppliers"]):
        if supplier.get("id") == supplier_id:
            fake_data["suppliers"][idx] = update_supplier
            break

    return update_supplier



@router.delete("/{supplier_id}", status_code=204)
def delete_supplier(supplier_id: int):
    supplier_with_id = create_list_with_id("suppliers")

    supplier = next((idx for idx, supplier in enumerate(supplier_with_id) if supplier["id"]== supplier_id), None)

    if supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not Found")
    
    del fake_data["suppliers"][supplier]

    return None
  
from fastapi import APIRouter, HTTPException
from app import fake_data
from ..schema.transaction_details import TransactionDetail, TransactionDetailCreate
from typing import List
from ..utils.commons import create_list_with_id



router = APIRouter(prefix="/transaction-details", tags=["Transaction details"])

@router.get("/", response_model=List[TransactionDetail])
async def get_transaction_details():
    return create_list_with_id("transaction_details")

@router.get("/{transaction_detail_id}", response_model=TransactionDetail)
def get_transaction_by_id(transaction_detail_id: int):
    transaction_detail_with_id = create_list_with_id("transaction_details")
    
    transaction_detail = next((transaction_detail for transaction_detail in transaction_detail_with_id if transaction_detail["id"]== transaction_detail_id), None)

    if transaction_detail is None:
        raise HTTPException(status_code=404, detail="Transaction detail not found")

    return transaction_detail

@router.post("/", response_model=TransactionDetail)
def create_transaction_details(transaction_detail: TransactionDetailCreate):

    transaction_detail_id = len(fake_data["transaction_details"]) + 1

    new_transaction_detail = transaction_detail.dict()
    new_transaction_detail["id"]= transaction_detail_id

    fake_data["transaction_details"].append(new_transaction_detail)

    return new_transaction_detail

@router.put("/{transaction_detail_id}", response_model=TransactionDetail)
def update_transaction_detail(transaction_detail_id: int, transaction: TransactionDetailCreate):

    transaction_detail_with_id = create_list_with_id("transaction_details")

    existing_transaction_detail_id = next((transaction_detail for transaction_detail in transaction_detail_with_id if transaction_detail["id"]== transaction_detail_id ), None)

    if existing_transaction_detail_id is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    update_transaction_detail = {**existing_transaction_detail_id, **transaction.dict()}

    for idx, transaction_detail in enumerate(fake_data["transaction_details"]):
        if transaction_detail.get("id") == transaction_detail_id:
            fake_data["transaction_details"][idx] = update_transaction_detail
            break

    return update_transaction_detail


@router.delete("/{transaction_detail_id}", status_code=204)
def delete_transaction_detail(transaction_detail_id: int):
    
    transaction_detail_with_id= create_list_with_id("transaction_details")

    transaction_detail = next((idx for idx, transaction_detail in enumerate(transaction_detail_with_id) if transaction_detail["id"]==transaction_detail_id), None)

    if transaction_detail is None:
        raise HTTPException(status_code=404, detail="transaction_detail is Found")
    
    del fake_data["transaction_details"][transaction_detail]
    
    return None

from fastapi import APIRouter, HTTPException
from app import fake_data
from ..utils.commons import create_list_with_id
from ..schema.transactions import Transaction, TransactionCreate
from typing import List

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/", response_model=List[Transaction])
async def get_transactions():
   return create_list_with_id("transactions")

@router.get("/{transaction_id}", response_model=Transaction)
def get_transactions_by_id(transaction_id: int):
    transaction_with_id = create_list_with_id("transactions")

    transaction = next((transaction for transaction in transaction_with_id if transaction["id"] ==transaction_id), None)

    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    return transaction

@router.post("/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate):

    transaction_id = len(fake_data["transactions"]) + 1

    new_transaction = transaction.dict()
    new_transaction["id"] = transaction_id
    
    fake_data["transactions"].append(new_transaction)

    return new_transaction

@router.put("/{transaction_id}", response_model=Transaction)
def update_transaction(transaction_id: int, transaction: TransactionCreate):
    transaction_with_id = create_list_with_id("transactions")

    existing_transaction = next((transaction for transaction in transaction_with_id if transaction["id"]== transaction_id), None)

    if existing_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    
    update_transaction = {**existing_transaction, **transaction.dict()}

    for idx, transaction in enumerate(fake_data["transactions"]):
        if transaction.get("id") == transaction_id:
            fake_data["transactions"][idx] = update_transaction
            break

    return update_transaction

@router.delete("/{transaction_id}", status_code=204)
def delete_transaction(transaction_id: int):
    
    transaction_with_id = create_list_with_id("transactions")

    transaction_index = next((idx for idx, transaction in enumerate(transaction_with_id) if transaction["id"]==transaction_id), None)

    if transaction_index is None:
        raise HTTPException(status_code=404, detail="Transaction not found")

    del fake_data["transactions"][transaction_index]

    return None
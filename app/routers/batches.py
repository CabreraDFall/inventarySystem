from fastapi import APIRouter, HTTPException
from app import fake_data
from typing import List
from ..schema.batches import Batch, BatchCreate

router = APIRouter(prefix="/batches", tags=["Batches"]) 

@router.get("/", response_model=List[Batch])
def get_users():
    batch_with_id =[
        {**batch, "id": idx+1}for idx, batch in enumerate(fake_data["batches"])
    ]
    return batch_with_id


@router.get("/{batch_id}")
def get_batch_by_id(batch_id:int):
    batch_with_id= [
       {**batch, "id": idx+1} for idx, batch in enumerate(fake_data["batches"])
    ]

    batch = next((batch for batch in batch_with_id if batch["id"]==batch_id),None)

    if batch is None:
       raise HTTPException(status_code=404, detail="Batch not found")
    
    return batch    

@router.post("/")
def create_batch(bacth:BatchCreate):
    
    batch_id = len(fake_data["batches"]) + 1

    new_batch = bacth.dict()
    new_batch["id"]= batch_id

    fake_data["batches"].append(new_batch)

    return new_batch


@router.put("/{batch_id}", response_model=Batch)
def update_batch(batch_id: int, batch: BatchCreate):
    batch_with_id =[
        {**batch, "id": idx+1}for idx, batch in enumerate(fake_data["batches"])
    ]

    exiting_batch = next((batch for batch in batch_with_id if batch["id"]== batch_id),None)

    if exiting_batch is None:
        raise HTTPException(status_code=404, detail="Bacth not found")
    
    update_batch = {**exiting_batch, **batch.dict()}

    for idx, batch in enumerate(fake_data["batches"]):
        if batch.get("id") == batch_id:
            fake_data["batches"][idx] = update_batch
            break
    return update_batch

@router.delete("/{batch_id}", status_code=204)
def delete_batch(batch_id: int):
    batch_with_id = [
        {**batch, "id": idx + 1 } for idx, batch in enumerate(fake_data["batches"])
    ]

    batch_index= next((idx for idx, batch in enumerate(batch_with_id) if batch["id"]==batch_id), None)

    if batch_index is None:
        raise HTTPException(status_code=404, detail="Batch not found")
    
    del fake_data["batches"][batch_index]
    
    return None

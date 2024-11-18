from fastapi import APIRouter, HTTPException
from app import fake_data
from ..schema.stock_history import StockHistory, StockHistoryCreate
from typing import List 


router = APIRouter(prefix="/stock-histories", tags=["Stock history"])


@router.get("/", response_model=List[StockHistory])
def get_users():
    stock_histories_with_id = [
        {**stock_history, "id": idx + 1} for idx, stock_history in enumerate(fake_data["stock_histories"])
    ]
    return stock_histories_with_id


@router.get("/{stock_history_id}", response_model=StockHistory)  # Obtener un usuario por ID
def get_user_by_id(stock_history_id: int):
    # Buscar el usuario con el ID especificado
    stock_histories_with_id = [
        {**stock_history, "id": idx + 1} for idx, stock_history in enumerate(fake_data["stock_histories"])
    ]
    # Buscar al usuario en la lista
    stock_history = next((stock_history for stock_history in stock_histories_with_id if stock_history["id"] == stock_history_id), None)
    
    if stock_history is None:
        # Si el usuario no se encuentra, lanzar una excepción HTTP 404
        raise HTTPException(status_code=404, detail="User not found")
    
    return stock_history

@router.post("/", response_model=StockHistory)  # Indicamos que la respuesta será un objeto User
def create_user(stock_history: StockHistoryCreate):
    # Generar un ID único para el nuevo usuario (por ejemplo, el siguiente número en la lista)
    stock_history_id = len(fake_data["stock_histories"]) + 1
    
    # Crear el nuevo usuario con los datos proporcionados
    new_stock_history = stock_history.dict()  # Convertimos el objeto StockHistoryCreate a un diccionario
    new_stock_history["id"] = stock_history_id  # Asignamos el ID generado
    
    # Guardar el nuevo usuario en la lista
    fake_data["stock_histories"].append(new_stock_history)
    
    # Devolver el nuevo usuario con el ID asignado
    return new_stock_history

@router.put("/{stock_history_id}", response_model=StockHistory)
def update_user(stock_history_id: int, stock_history: StockHistoryCreate):
    # Asignar un ID a cada usuario de fake_data["users"] antes de devolverlo
    stock_histories_with_id = [
        {**stock_history, "id": idx + 1} for idx, stock_history in enumerate(fake_data["stock_histories"])
    ]

    # Buscar al usuario con el ID especificado
    existing_stock_history = next((stock_history for stock_history in stock_histories_with_id if stock_history["id"] == stock_history_id), None)
    
    if existing_stock_history is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Actualizar los campos del usuario encontrado
    updated_stock_histories = {**existing_stock_history, **stock_history.dict()}  # Actualizamos los campos con el nuevo valor
    
    # Reemplazar el usuario en la lista
    for idx, stock_history in enumerate(fake_data["stock_histories"]):
        if stock_history.get("id") == stock_history_id:
            fake_data["stock_histories"][idx] = updated_stock_histories
            break
    
    # Devolver el usuario actualizado
    return updated_stock_histories

# Endpoint para eliminar un usuario por su ID
@router.delete("/{stock_history_id}", status_code=204)
def delete_user(stock_history_id: int):
    # Buscar al usuario con el ID especificado
    stock_histories_with_id = [
        {**stock_history, "id": idx + 1} for idx, stock_history in enumerate(fake_data["stock_histories"])
    ]
    
    
    # Buscar el usuario en la lista
    stock_history_index = next((idx for idx, stock_history in enumerate(stock_histories_with_id) if stock_history["id"] == stock_history_id), None)
    
    if stock_history_index is None:
        # Si el usuario no existe, lanzar un error 404
        raise HTTPException(status_code=404, detail="User not found")
    
    # Eliminar el usuario de la lista
    del fake_data["stock_histories"][stock_history_index]
    
    # No es necesario devolver nada. FastAPI automáticamente responderá con 204 No Content
    return None
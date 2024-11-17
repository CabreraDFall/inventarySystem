# items.py
from fastapi import APIRouter, HTTPException
from app import fake_data
from ..schema.user import User, UserCreate
from typing import List 

router = APIRouter(prefix="/users", tags=["Users"]) 

@router.get("/", response_model=List[User])
def get_users():
    users_with_id = [
        {**user, "id": idx + 1} for idx, user in enumerate(fake_data["users"])
    ]
    return users_with_id


@router.get("/{user_id}", response_model=User)  # Obtener un usuario por ID
def get_user_by_id(user_id: int):
    # Buscar el usuario con el ID especificado
    users_with_id = [
        {**user, "id": idx + 1} for idx, user in enumerate(fake_data["users"])
    ]
    
    # Buscar al usuario en la lista
    user = next((user for user in users_with_id if user["id"] == user_id), None)
    
    if user is None:
        # Si el usuario no se encuentra, lanzar una excepción HTTP 404
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.post("/", response_model=User)  # Indicamos que la respuesta será un objeto User
def create_user(user: UserCreate):
    # Generar un ID único para el nuevo usuario (por ejemplo, el siguiente número en la lista)
    user_id = len(fake_data["users"]) + 1
    
    # Crear el nuevo usuario con los datos proporcionados
    new_user = user.dict()  # Convertimos el objeto UserCreate a un diccionario
    new_user["id"] = user_id  # Asignamos el ID generado
    
    # Guardar el nuevo usuario en la lista
    fake_data["users"].append(new_user)
    
    # Devolver el nuevo usuario con el ID asignado
    return new_user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate):
    # Asignar un ID a cada usuario de fake_data["users"] antes de devolverlo
    users_with_id = [
        {**user, "id": idx + 1} for idx, user in enumerate(fake_data["users"])
    ]
    
    # Buscar al usuario con el ID especificado
    existing_user = next((user for user in users_with_id if user["id"] == user_id), None)
    
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Actualizar los campos del usuario encontrado
    updated_user = {**existing_user, **user.dict()}  # Actualizamos los campos con el nuevo valor
    
    # Reemplazar el usuario en la lista
    for idx, user in enumerate(fake_data["users"]):
        if user.get("id") == user_id:
            fake_data["users"][idx] = updated_user
            break
    
    # Devolver el usuario actualizado
    return updated_user

# Endpoint para eliminar un usuario por su ID
@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    # Buscar al usuario con el ID especificado
    users_with_id = [
        {**user, "id": idx + 1} for idx, user in enumerate(fake_data["users"])
    ]
    
    # Buscar el usuario en la lista
    user_index = next((idx for idx, user in enumerate(users_with_id) if user["id"] == user_id), None)
    
    if user_index is None:
        # Si el usuario no existe, lanzar un error 404
        raise HTTPException(status_code=404, detail="User not found")
    
    # Eliminar el usuario de la lista
    del fake_data["users"][user_index]
    
    # No es necesario devolver nada. FastAPI automáticamente responderá con 204 No Content
    return None
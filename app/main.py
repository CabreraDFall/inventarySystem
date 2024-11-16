# main.py
from fastapi import FastAPI
from app.routers import users_router,products_router, batches_router,categories_router, stock_history_router, suppliers_router, transaction_details_router, transactions_router
  # Importamos el router de items

app = FastAPI(
        title="Invetory system", 
        openapi_tags=[
            {"name": "Home", "description": "Las rutas principales del sistema"},
            {"name": "Users", "description": "Usuarios"},
            {"name": "Categories", "description": "Lotes"},
            {"name": "Products", "description": "Lotes"},
            {"name": "Stock history", "description": "Lotes"},
            {"name": "Suppliers", "description": "Lotes"},
            {"name": "Transactions", "description": "Lotes"},
            {"name": "Transaction details", "description": "Lotes"},
    ])

# Incluir el router
app.include_router(users_router)
app.include_router(products_router)
app.include_router(categories_router)
app.include_router(stock_history_router)
app.include_router(suppliers_router)
app.include_router(transaction_details_router)
app.include_router(transactions_router)





@app.get("/",  tags=["Home"])
def read_root():
    return {"message": "Hola, Mundo!"}
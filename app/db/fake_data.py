fake_data ={
  "users": [
    {
      "username": "jdoe123",
      "email": "jdoe123@example.com",
      "full_name": "John Doe"
    },
    {
      "username": "maria_smith",
      "email": "maria.smith@example.com",
      "full_name": "Maria Smith"
    },
    {
      "username": "alex_w",
      "email": "alex.williams@example.com",
      "full_name": None
    }
  ],
  "products": [
    {
      "name": "Laptop",
      "description": "Una laptop potente para trabajar y jugar.",
      "price": 999.99,
      "stock": 50
    },
    {
      "name": "Smartphone",
      "description": "Smartphone con una cámara de alta calidad.",
      "price": 599.99,
      "stock": 100
    },
    {
      "name": "Teclado Mecánico",
      "description": None,
      "price": 120.0,
      "stock": 200
    }
  ],
  "categories": [
    {
      "name": "Electrónica",
      "description": "Productos electrónicos como computadoras, teléfonos y accesorios."
    },
    {
      "name": "Muebles",
      "description": "Muebles para hogar y oficina, como sillas, mesas y estanterías."
    },
    {
      "name": "Ropa",
      "description": "Ropa de moda y accesorios."
    }
  ],
  "stock_histories": [
    {
      "product_id": 1,
      "quantity_changed": 20,
      "transaction_type": "entrada",
      "change_date": "2024-11-16T10:00:00"
    },
    {
      "product_id": 2,
      "quantity_changed": -10,
      "transaction_type": "salida",
      "change_date": "2024-11-15T14:30:00"
    },
    {
      "product_id": 3,
      "quantity_changed": 50,
      "transaction_type": "entrada",
      "change_date": "2024-11-14T09:00:00"
    }
  ],
  "suppliers": [
    {
      "name": "Proveedor A",
      "contact_name": "Juan Pérez",
      "phone_number": "+1234567890",
      "email": "juan.perez@proveedora.com"
    },
    {
      "name": "Proveedor B",
      "contact_name": "Ana García",
      "phone_number": "+0987654321",
      "email": "ana.garcia@proveedorb.com"
    },
    {
      "name": "Proveedor C",
      "contact_name": None,
      "phone_number": "+1122334455",
      "email": None
    }
  ],
  "transaction_details": [
    {
      "transaction_id": 1,
      "product_id": 1,
      "quantity": 5,
      "price": 999.99
    },
    {
      "transaction_id": 1,
      "product_id": 2,
      "quantity": 2,
      "price": 599.99
    },
    {
      "transaction_id": 2,
      "product_id": 3,
      "quantity": 3,
      "price": 120.0
    }
  ],
  "transactions": [
    {
      "transaction_type": "compra",
      "total_amount": 2199.95,
      "transaction_date": "2024-11-16T10:00:00"
    },
    {
      "transaction_type": "venta",
      "total_amount": 1800.0,
      "transaction_date": "2024-11-15T14:30:00"
    }
  ],
  "batches": [
    {
      "product_id": 1,
      "quantity": 30,
      "batch_code": "BATCH001",
      "expiration_date": "2025-12-31"
    },
    {
      "product_id": 2,
      "quantity": 50,
      "batch_code": "BATCH002",
      "expiration_date": None
    },
    {
      "product_id": 3,
      "quantity": 100,
      "batch_code": "BATCH003",
      "expiration_date": "2024-06-30"
    }
  ]
}



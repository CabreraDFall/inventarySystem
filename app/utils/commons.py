from app import fake_data

def create_list_with_id(where: str) -> list:
    id_generate =[
        {**list_generate, "id": idx+1 }for idx, list_generate in enumerate(fake_data[where])
    ]
    return id_generate
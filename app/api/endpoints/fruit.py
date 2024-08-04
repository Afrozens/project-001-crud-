from fastapi import APIRouter, status

router = APIRouter()

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_fruit(data):
    pass
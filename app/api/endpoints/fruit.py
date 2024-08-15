from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.controller import fruit as fruit_controller
from app.core.database import get_session
from app.schemas.fruits import FruitCreate, FruitInDbBase, FruitUpdate

router = APIRouter()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=FruitInDbBase)
async def get_fruit (id: str, session: Session = Depends(get_session)):
    fruit_current = await fruit_controller.get_fruit(id, session)
    return fruit_current

@router.get('/all', status_code=status.HTTP_200_OK)
async def get_all_fruit(session: Session = Depends(get_session)):
    fruit_all = await fruit_controller.all_fruits(session)
    return fruit_all

@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_fruit(data: FruitCreate, session: Session = Depends(get_session)):
    await fruit_controller.create_fruit(data, session)
    return JSONResponse({'message': 'Fruit Created Congratulations'})

@router.put('/update/{id}', status_code=status.HTTP_200_OK)
async def update_fruit(id: str, data: FruitUpdate, session: Session = Depends(get_session)):
    pass
    
@router.delete('/delete/{id}', status_code=status.HTTP_200_OK)
async def delete_fruit(id: str, session: Session = Depends(get_session)):
    pass


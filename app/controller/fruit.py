from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.models.fruits import Fruit
from app.schemas.fruits import FruitCreate, FruitUpdate
from app.services.base import CRUDBase


class ControllerFruit(CRUDBase[Fruit, FruitCreate, FruitUpdate]):
    async def get_fruit(self, id: str, session: Session):
        try: 
            fruit_current = session.query(self.model).where(self.model.id == id).first()
            if not fruit_current:
                raise HTTPException(status_code=404, detail='Not Found Fruit')
            return fruit_current
        except Exception as error:
            raise HTTPException(status_code=500, detail=f'Hay un error: {str(error)}')
        
    async def all_fruits(self, session: Session):
        try:
          fruits = session.query(self.model).all() 
          if not fruits:
                raise HTTPException(status_code=404, detail='Not Found Fruit')

          if len(fruits) < 1:
                raise HTTPException(status_code=404, detail='Not Found Fruit')
          return fruits
      
        except Exception as error:
            raise HTTPException(status_code=500, detail=f'Hay un error: {str(error)}')
    
    async def create_fruit(self, data: FruitCreate, session: Session):
        try:
            db_obj = Fruit(**data.model_dump(exclude_unset=True))
            self.create(db=session, obj_in=db_obj)
        except Exception as error:
            raise HTTPException(status_code=500, detail=f'Hay un error: {str(error)}')

    async def update_fruit(self, id: str, data: FruitUpdate, session: Session):
        try: 
            fruit_current = await self.get_fruit(id, session)     
            self.update(db=session, db_obj=fruit_current, obj_in=data)
        except Exception as error:
            raise HTTPException(status_code=500, detail=f'Hay un error: {str(error)}')


fruit = ControllerFruit()
fruit.model = Fruit

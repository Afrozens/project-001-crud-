from  app.core.database import Base
from uuid import uuid4 
from sqlalchemy import Boolean, Column, DateTime, String, func, Text, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Fruit(Base):
    __tablename__= 'fruits'

    id= Column( 
        UUID(150), primary_key=True, index= True, default=uuid4
    )
    
    name = Column(String(150))
    description = Column(Text)
    price = Column(Integer)
    featured = Column(Boolean, default=False)
    finish_line_at = Column(DateTime)
    place = Column(String(150),nullable=True)
    
    created_at = Column(DateTime, nullable=False, server_default=func.now())

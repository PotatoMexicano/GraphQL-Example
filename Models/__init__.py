from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from Connection import Base, Session
import strawberry
from typing import Optional, Literal

session = Session()

@strawberry.type
class User(Base):

    __tablename__ = 'usuario'

    id:int = Column('_id', Integer, primary_key=True, nullable=False)
    nome_completo:str = Column('nome_completo', String, nullable=False)
    email:str = Column('email', String, nullable=False)
    login:str = Column('login', String, nullable=False)
    id_status:int = Column('id_status', Integer, nullable=False)
    nivel_acesso:int = Column('nivel_acesso', Integer, nullable=False)
    ultimo_login: Optional[datetime] = Column('ultimo_login', DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<User: {self.nome_completo}>"
    
    def select(id:int):
        response = session.query(User).filter(User.id == id).one_or_none()
        if not response:
            return None
        return response
    
    def selectAll() -> list:
        response = session.query(User).all()
        return response

@strawberry.type
class Query:
    @strawberry.field
    async def selectAll(self) -> list[User]:
        return User.selectAll()
    
    @strawberry.field
    async def selectOne(self, id:int) -> Optional[User]:
        return User.select(id=id)
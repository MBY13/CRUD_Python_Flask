from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///users.db')
Session = sessionmaker(bind=engine)
session = Session()  # Cria uma única sessão

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        session.add(self)  # Adiciona a instância à sessão existente
        session.commit()

    def update(self):
        session.commit()

    def delete(self):
        session.delete(self)
        session.commit()

    @staticmethod
    def get_all():
        return session.query(User).all()

    @staticmethod
    def get_by_id(user_id):
        return session.query(User).filter_by(id=user_id).first()

Base.metadata.create_all(engine)  # Cria as tabelas no banco de dados

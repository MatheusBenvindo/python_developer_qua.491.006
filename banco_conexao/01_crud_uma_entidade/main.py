from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base 


try:
    engine = create_engine('sqlite:///01_crud_uma_entidade/database/db_crud.db')
    Base = declarative_base()

    #NOTE - engine para o mysql
    #engine = create_engine('mysql+mysqlconnector://root:senha@localhost:3306/nome_do_banco')
    print("Conexão bem-sucedida!")

    class Pessoa(Base):
        __tablename__ = 'pessoas'

        id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
        nome = Column(String, nullable=False)
        email = Column(String, nullable=False, unique=True)
        data_nascimento = Column(Date, nullable=False)

    Base.metadata.create_all(engine)
    print("Tabela criada com sucesso!")

    
except Exception as e:
    print(f"Erro: {e}")

    #prepared statement
    #sql injection
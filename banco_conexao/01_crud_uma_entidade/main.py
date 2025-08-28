# importa a biblioteca sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import os 

limpar = lambda: os.system("cls")

def criar_tb_pessoa(engine, Base):
    try:
        class Pessoa(Base):
            __tablename__ = "pessoa"

            id_pessoa = Column(Integer, primary_key=True, autoincrement=True)
            nome = Column(String, nullable=False)
            email = Column(String, nullable=False, unique=True)
            data_nascimento = Column(Date, nullable=False)

        Base.metadata.create_all(engine)
    # NOTE:  engine para o MySQL
    # engine = create_engine("mysql+mysqlconnector://senha:root@localhost:3306/nome_banco")
        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar ao banco. {e}")

def cadastrar_pessoa(session, Pessoa):
    nome = input("Nome: ").strip().title()
    email = input("Email: ").strip().lower()
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

    session.add(nova_pessoa)
    session.commit()
    print (f"pessoa {nome} cadastrada com sucesso")

def main():
    engine = create_engine("sqlite:///01_crud_uma_entidade/database/db_crud.db")
    Base = declarative_base()

    Pessoa = criar_tb_pessoa(engine, Base)

    Session = sessionmaker(bind=engine)
    session = Session()

    limpar()
    while True:
        print(f"{'='*30}\nCRUD\n{'='*30}")
        print("1 - Cadastrar nova pessoa")
        print("2 - Listar pessoas")
        print("3 - alterar dados de uma pessoa")
        print("4 - Excluir uma pessoa")
        print("5 - Sair do programa")
        cadastrar_pessoa(session, Pessoa)
        opcao = input("Informe a opção desejada.")
        limpar()
    
        match opcao:
            case "1":
                cadastrar_pessoa(session, Pessoa)
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                print("Saindo do programa...")
                break
            case "_":
                print("Opção inválida. Tente novamente.")
                continue
    
if __name__ == "__main__":  # Corrigido aqui
    main()
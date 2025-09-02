from datetime import datetime
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def cadastrar_pessoa(session, Pessoa):
    try:
        nome = input("Digite o nome do usuário: ").strip().title()
        email = input("Digite o e-mail do usuário: ").strip().lower()

        # Correção do filtro por e-mail
        pessoa_existente = session.query(Pessoa).filter(Pessoa.email == email).first()

        if pessoa_existente:
            print("E-mail já cadastrado.")
        else:
            data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ").strip()
            try:
                data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            except ValueError:
                print("Data em formato inválido. Use dd/mm/aaaa.")
                return

            nova_pessoa = Pessoa(nome=nome, email=email, data_nascimento=data_nascimento)

            session.add(nova_pessoa)
            session.commit()

            print(f"Pessoa {nome} cadastrada com sucesso.")
    except Exception as e:
        print(f"Não foi possível cadastrar pessoa. {e}.")

def listar_pessoas(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()

        print("\nPessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print(f"{'-'*40}")
    except Exception as e:
        print(f"Não foi possível listar pessoas. {e}.")

def pesquisar_pessoas(session, Pessoa):
    print("Filtrar pessoas por campo:")
    print("1 - ID")
    print("2 - Nome")
    print("3 - E-mail")
    print("4 - Data de nascimento")
    print("5 - Retornar")
    campo = input("Escolha o campo a ser pesquisado: ").strip()
    limpar()

    pessoas = []
    match campo:
        case "1":
            valor = input("Digite o ID para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.id_pessoa.like(f"{valor}")).all()
        case "2":
            valor = input("Digite o nome para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.nome.like(f"%{valor}%")).all()
        case "3":
            valor = input("Digite o e-mail para buscar: ").strip()
            pessoas = session.query(Pessoa).filter(Pessoa.email.like(f"%{valor}%")).all()
        case "4":
            valor = input("Digite a data de nascimento (dd/mm/aaaa) para buscar: ").strip()
            try:
                data_nascimento = datetime.strptime(valor, "%d/%m/%Y").date()
                pessoas = session.query(Pessoa).filter(Pessoa.data_nascimento == data_nascimento).all()
            except ValueError:
                print("Data em formato inválido. Use dd/mm/aaaa.")
        case "5":
            return
        case _:
            print("Campo inexistente.")
            return

    limpar()
    print("\nResultado da pesquisa:\n")
    if pessoas:
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"E-mail: {pessoa.email}")
            print(f"Data de Nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
            print(f"{'-'*40}")
    else:
        print("Nenhuma pessoa foi encontrada.")

def alterar_dados(session, Pessoa):
    try:
        print("Escolha por qual dado deseja fazer a busca e alteração.")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Retornar")
        opcao = input("Escolha o campo que deseja pesquisar: ").strip()
        limpar()

        pessoa = None
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email_consulta = input("Informe o e-mail: ").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email_consulta).first()
            case "3":
                return
            case _:
                print("Opção inválida")
                return

        if pessoa:
            novo_nome = None
            novo_email = None
            nova_data_nascimento = None

            while True:
                print("Qual campo deseja alterar:\n")
                print(f"ID {pessoa.id_pessoa}")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.data_nascimento.strftime('%d/%m/%Y')}")
                print("4 - Finalizar.")
                campo = input("Informe o campo que deseja alterar: ").strip()
                limpar()
                match campo:
                    case "1":
                        novo_nome = input("Informe o novo nome: ").strip().title()
                        print(f"Nome a ser cadastrado: {novo_nome}.")
                        continue
                    case "2":
                        novo_email = input("Informe o novo e-mail: ").strip().lower()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        if pessoas and novo_email != pessoa.email:
                            print("E-mail já cadastrado.")
                        else:
                            print(f"E-mail a ser cadastrado: {novo_email}.")
                        continue
                    case "3":
                        nova_data_nascimento_input = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        try:
                            nova_data_nascimento = datetime.strptime(nova_data_nascimento_input, "%d/%m/%Y").date()
                            print(f"Data de nascimento a ser cadastrada: {nova_data_nascimento.strftime('%d/%m/%Y')}.")
                        except ValueError:
                            print("Data inválida. Use o formato dd/mm/aaaa.")
                        continue
                    case "4":
                        break
                    case _:
                        print("Campo inexistente")
                        continue

            pessoa.nome = novo_nome if novo_nome else pessoa.nome
            pessoa.email = novo_email if novo_email else pessoa.email
            pessoa.data_nascimento = nova_data_nascimento if nova_data_nascimento else pessoa.data_nascimento
            session.commit()

            print("Pessoa alterada com sucesso!")
        else:
            print("Pessoa não encontrada.")
    except Exception as e:
        print(f"Não foi possível alterar. {e}.")

def excluir_pessoa(session, Pessoa):
    try:
        print("Escolha o campo para selecionar a pessoa a ser excluída")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Desistir")
        opcao = input("Informe o campo que deseja pesquisar: ").strip()
        limpar()

        pessoa = None
        match opcao:
            case "1":
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email_consulta = input("Informe o e-mail: ").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email_consulta).first()
            case "3":
                return
            case _:
                print("Opção inválida")
                return

        if pessoa:
            print(f"Pessoa encontrada: {pessoa.nome} ({pessoa.email})")
            confirmacao = input("Tem certeza que deseja excluir? (s/n): ").strip().lower()
            if confirmacao == "s":
                session.delete(pessoa)
                session.commit()
                print("Pessoa excluída com sucesso!")
            else:
                print("Exclusão cancelada.")
        else:
            print("Pessoa não encontrada.")
    except Exception as e:
        print(f"Não foi possível excluir pessoa. {e}.")


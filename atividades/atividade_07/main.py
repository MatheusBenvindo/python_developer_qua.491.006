"""
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista.
- Liste todos os nomes na lista.
- Pesquise por um nome na lista.
- Altere um nome na lista.
- Exclua um nome na lista.
- Sair do programa

#NOTE - a lista deve começar vazia. exemplo:
lista = []

"""

import os 

lista = []

menu = """
-------------------- MANIPULAÇÃO DE LISTAS --------------------
1 - Cadastre novo nome na lista.
2 - Liste todos os nomes na lista.
3 - Pesquise por um nome na lista.
4 - Altere um nome na lista.
5 - Exclua um nome na lista.
6 - Sair do programa.
7 - Retornar ao começo.
--------------------------------------------------------------
"""

print(menu)

operador = int(input("Digite o que deseja fazer: "))

match operador:
    # CADASTRO DE NOME
    case "1":
        try:
            novo_item = input("Informe o novo nome para cadastrar: ").title().strip()
            if novo_item:
                lista.append(novo_item)
                print("Nome inserido com sucesso.")
            else:
                print("Nome não pode ser vazio.")
        except Exception as e:
            print(f"Não foi possível cadastrar o nome: {e}")
        finally:
            os.system("cls")
            print(lista)
            int(input(f"O que deseja fazer agora? {menu}"))     
    case "2":
        try:
            print(lista)
        except Exception as e:
            print(f"Não foi possivel exibir. Confira o nome da lista e tente novamente.{e}")
        finally:
            os.system("cls")
            print(lista)
            int(input(f"O que deseja fazer agora? {menu}")) 
    case "3":
        try:
            ...
        except Exception as e:
            ...
    case "4":
        try:
            ...
        except Exception as e:
            ...
    case "5":
        try:
            ...
        except Exception as e:
            ...
    case "6":
        try:
            ...
        except Exception as e:
            ...
    case "7":
        try:
            ...
        except Exception as e:
            ...




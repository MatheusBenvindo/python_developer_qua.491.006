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
--------------------------------------------------------------
"""

print(menu)


while True:
    os.system("cls")
    print(lista)
    print(menu)

    try:
        operador = int(input("Digite o que deseja fazer: "))
    except Exception as e:
        print("Digite um número válido.")
        continue

    match operador:
        # CADASTRO DE NOME
        case 1:
            try:
                novo_item = (
                    input("Informe o novo nome para cadastrar: ").title().strip()
                )
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
        # LISTAGEM DE NOMES
        case 2:
            try:
                print(lista)
            except Exception as e:
                print(
                    f"Não foi possivel exibir. Confira o nome da lista e tente novamente.{e}"
                )
            finally:
                os.system("cls")
                print(lista)
        # PESQUISA DE NOME
        case 3:
            try:
                input("Informe o nome que deseja pesquisar:").title().strip()
                if input in lista:
                    print(
                        f"Nome encontrado, {input}!, está na posição {lista.index(input)}"
                    )
                else:
                    print("Nome não encontrado na lista.")
            except Exception as e:
                print(f"Não foi possivel pesquisar o nome na lista.{e}")
            finally:
                os.system("cls")
                print(lista)
        # ALTERAÇÃO DE NOME
        case 4:
            try:
                for i in range(len(lista)):
                    print(f"{i} - {lista[i]}")
                posicao = int(input("Informe a posição do nome que deseja alterar: "))
                if 0 <= posicao < len(lista):
                    novo_nome = input("Informe o novo nome: ").title().strip()
                    if novo_nome:
                        lista[posicao] = novo_nome
                        print("Nome alterado com sucesso.")
                    else:
                        print("Nome não pode ser vazio.")
                else:
                    print("Posição inválida.")
            except Exception as e:
                print(f"Não foi posssivel alterar o nome {e}.")
            finally:
                os.system("cls")
                print(lista)
        # EXCLUSÃO DE NOME
        case 5:
            try:
                for i in range(len(lista)):
                    print(f"{i} - {lista[i]}")
                posicao = int(input("Informe a posição do nome que deseja excluir: "))
                if 0 <= posicao < len(lista):
                    del lista[posicao]
                    print(f"Nome excluído com sucesso.")
                else:
                    print("Posição inválida.")
            except Exception as e:
                print(f"Não foi possivel excluir o nome {e}.")
            finally:
                os.system("cls")
                print(lista)
        # SAIR DO PROGRAMA
        case 6:
            try:
                print("Saindo do programa...")
                exit()
            except Exception as e:
                print(f"Não foi possivel sair do programa {e}.")
        case _:
            try:
                print("Opção inválida. Tente novamente.")
            except Exception as e:
                print(f"Erro ao processar a opção: {e}")
            finally:
                os.system("cls")
                print(lista)

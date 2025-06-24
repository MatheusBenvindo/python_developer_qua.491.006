import os

lista = [
    "Ana",
    "Bruno",
    "Carlos",
    "Daniela",
    "Eduardo",
    "Fernanda",
    "Gabriel",
    "Helena",
    "Igor",
    "Juliana",
    "Kleber",
    "Larissa",
    "Marcos",
    "Natália",
    "Otávio",
    "Paula",
    "Quésia",
    "Rafael",
    "Sofia",
    "Tiago"
]

#remover itens de uma lista.

for i in range(len(lista)):
    print(f"{i}: {lista[i]}.")

try:
    i = int(input(f"Informe a posição do item: "))
    if i >= 0 and i < len(lista):
        del(lista[i])
        print ("Nome excluido com sucesso!")
    else:
        print ("Posição inválida")
except Exception as e:
    print (f"Não foi possivel excluir o nome da lista {e}.")
finally:
    for i in range (len(lista)):
        print(f"{i}: {lista[i]}")


#lista.remove("Carlos") removendo nome especifico de acordo com o conteudo.


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

lista = []



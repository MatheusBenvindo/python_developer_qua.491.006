import os

os.system('cls')

while True:
    nome = input("informe seu nome: ")
    os.system('cls')
    print(f"Seja bem vindo, {nome}")
    
    prosseguir = input("Deseja inserir outro nome? S/N ").lower().strip()

    match prosseguir:
        case "s":
            os.system("cls")
        case "n":
            break
        case _:
            print("Opção Inválida")
            break
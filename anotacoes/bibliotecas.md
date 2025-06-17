OS = importações para comandos do sistema operacional (qualquer que seja).

os.system ("CLS") = clear (WINDOWS) - Limpa o terminal antes de prosseguir para a próxima linha/instrução.

os.system ("") - Executa qualquer comando que esteja entre as "

alias = apelidar um comando import x as xx
uso: xx.function

import os
import math

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    print("Menu:")
    print("1 - Calcular área de um círculo")
    print("2 - Calcular tamanho de uma circunferência")
    print("3 - Sair do programa")

while True:
    limpar_terminal()
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        raio = float(input("Digite o raio do círculo: "))
        area = math.pi * raio ** 2
        print(f"Área do círculo: {area:.2f}")
        input("Pressione Enter para continuar...")
    elif escolha == '2':
        raio = float(input("Digite o raio da circunferência: "))
        circunferencia = 2 * math.pi * raio
        print(f"Tamanho da circunferência: {circunferencia:.2f}")
        input("Pressione Enter para continuar...")
    elif escolha == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")
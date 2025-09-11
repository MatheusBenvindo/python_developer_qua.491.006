import os
import math as m

while True:
    os.system("cls")
    print(
        "Selecione uma opção\n"
        "1 - Calcular área de um círculo\n"
        "2 - Calcular tamanho de uma circunferência\n"
        "3 - Sair do programa\n"
    )
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        raio = float(input("Digite o raio do círculo: "))
        area = m.pi * m.pow(raio, 2)
        print(f"Área do círculo: {area:.2f}")
        input("Pressione Enter para continuar...")
    elif escolha == '2':
        raio = float(input("Digite o raio da circunferência: "))
        circunferencia = 2 * m.pi * raio
        print(f"Tamanho da circunferência: {circunferencia:.2f}")
        input("Pressione Enter para continuar...")
    elif escolha == '3':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida.")
        input("Pressione Enter para continuar...")

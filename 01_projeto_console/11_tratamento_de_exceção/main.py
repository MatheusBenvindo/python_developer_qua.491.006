
import os
os.system("cls")

#tratamento de exceção
try:


    n = int(input("informe um numero inteiro: "))
    print(f"numero informado: {n}.")

except Exception as e:
    print(f"Não foi possivel exibir o número.{e}.")

finally:
    print("Programa encerrado com sucesso!")


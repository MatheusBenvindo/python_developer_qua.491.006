import math as m
import os

os.system ("cls")

print (f"o numero do pi: {m.pi:.2f}")

os.system ("cls")
try:
    n = int(input("informe um número inteiro "))
    os.system ("cls")

    print(f"A raiz quadrada de {n} é {m.sqrt(n):.2f}.")
except Exception as e:
    print ("Não foi possivel calcular a raiz quadrada. {e}")
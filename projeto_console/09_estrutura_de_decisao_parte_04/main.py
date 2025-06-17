#otimização
#operador ternário
import os 

os.system('cls')

nome = input("Qual é o seu nome?")
idade = int(input("Qual é a sua idade?"))

#operador ternário
result = "é maior de idade" if idade >= 18 else "não é maior de idade"

print (f"{nome} {result}")
import os 

os.system('cls')

nome = input("Qual é o seu nome?")
idade = int(input("Qual é a sua idade?"))


if idade >= 18: #Qual a condição? 
    print(f"Bem-vindo(a), {nome}") #O que acontece se a condição for satisfeita?

elif idade <= 0 or idade > 120: #Qual a condição?
    print("Idade inválida.")

else: #O que acontece se a condição não for satisfeita?
    print(f"Acesso negado, {nome} não tem idade suficiente para acessar o sistema.")
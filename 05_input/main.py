import os
os.system("cls")

#entrada de dados
nome = input("Infome seu nome: ")
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura em metros: ").replace(',', '.'))

#Saida de dados
print(f"Seja bem vindo ao curso de python, {nome}!")
print(f"Idade do usuário: {idade}.")
print(f"Altura do usuário: {altura}.")

#VERIFICANDO O TIPO DE DADOS
print(f"{nome}: {type(nome)}")
print(f"{idade}: {type(idade)}")
print(f"{altura}: {type(altura)}")
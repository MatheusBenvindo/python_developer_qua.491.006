import os 

os.system('cls')

nome = input("Qual é o seu nome?")
altura = float(input("Qual é a sua altura em metros?").replace(',', '.'))  # Substitui vírgula por ponto para aceitar decimal
idade = int(input("Qual é a sua idade?"))
            
if altura >= 1.15 and idade >=12:  # Qual a condição? Condicionais AND, NOT, OR 
    print(f"Parabéns {nome} Você pode entrar na montanha-russa, seja bem-vindo!")
else:
    print (f"Desculpe {nome}, você não pode entrar na montanha-russa.")

    
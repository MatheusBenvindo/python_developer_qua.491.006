"""# TODO - atividade: Crie um programa que recebe do usuário o nome e a idade, e em seguida, mostre um menu de filmes com suas respectivas classificações indicativas e salas de exibição. Exemplo:
- Sala 1: A Roda Quadrada - Livre
- Sala 2: A Volta dos Que Não Foram - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
O usuário deve escolher a sala que está passando o filme que deseja assistir.
- Se o usuário tiver a idade mínima ou mais para ver o filme, o programa imprime o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora da compra do ingresso, e deseje bom filme, e em seguida, encerra o programa.
- Se o usuário não tiver a idade mínima para ver o filme, o programa bloqueia a sua entrada, e re-exibe o menu de filmes para que ele escolha outro filme."""
import os 
import datetime
from datetime import date

#formatando data e hora
data = date.today().strftime("%d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M:%S")

sala1 = "A Roda Quadrada"
sala2 = "A Volta Dos Que Não Foram"
sala3 = "Poeira Em Alto Mar"
sala4 = "As Tranças Do Rei Careca"
sala5 = "A Vingança Do Peixe Frito"

try:
    nome = input("Informe o seu nome: ").title().strip()
    idade = int(input("Informe sua idade: "))

    while True:
        print(f"{'-'*20} CINE COBRA {'-'*20}")
        print(f"Sala 1 - {sala1} - Livre")
        print(f"Sala 2 - {sala2} - 12 anos") 
        print(f"Sala 3 - {sala3} - 14 anos") 
        print(f"Sala 4 - {sala4} - 16 anos") 
        print(f"Sala 5 - {sala5} - 18 anos") 
        sala = input("Informe a sala desejada: ").strip()

        os.system ("cls" if os.name =="nt" else "clear")

        match sala:
            case "1":
                idade_minima = 0
                filme = sala1
            case "2":
                idade_minima = 12
                filme = sala2
            case "3":
                idade_minima = 14
                filme = sala3
            case "4":
                idade_minima = 16
                filme = sala4
            case "5":
                idade_minima = 18
                filme = sala5
            case "_":
                print("Sala inexistente, favor escolher outra sala.")
                continue
        
        if idade >=idade_minima:
            print (f"{'-'*20} INGRESSO CINE COBRA {'-'*20} \n")
            print (f'{'-'*60}')
            print (f"Filme : {filme} - {idade_minima}")
            print (f"Ingresso comprado por {nome} dia {data} às {hora}.")
            print (f"Tenha um bom filme!")
            print (f'{'-'*60}')
            break
            
        else:
            print (f" {nome} não tem idade suficiente para assistir a {filme}.")
            print("Favor escolher outro filme.")
            continue
            

except Exception as e:
    print(f"Não foi possivel comprar ingresso {e}")



"""
import os 
import datetime

os.system("cls")
nome = input("Informe o seu nome: ").title().strip()
idade = int(input("Digite sua idade: "))

os.system("cls")
print (
-----------------------------------------------------
Sala 1: A Roda Quadrada - Livre
Sala 2: A Volta Dos Que Não Foram - 12 anos
Sala 3: Poeira em Alto Mar - 14 anos
Sala 4: As Tranças Do Rei Careca - 16 anos
Sala 5: A Vingança Do Peixe Frito - 18 anos
-----------------------------------------------------)


filmes = {
    1: {"nome": "A Roda Quadrada", "classificacao": 0, "sala": 1},
    2: {"nome": "A Volta Dos Que Não Foram", "classificacao": 12, "sala": 2},
    3: {"nome": "Poeira em Alto Mar", "classificacao": 14, "sala": 3},
    4: {"nome": "As Tranças Do Rei Careca", "classificacao": 16, "sala": 4},
    5: {"nome": "A Vingança Do Peixe Frito", "classificacao": 18, "sala": 5}
}

while True:
    try:
        filme = int(input("Escolha a sala qual contenha o filme que deseja assistir: (De 1 á 5) "))
        if filme not in filmes:
            print("Sala inválida. Tente novamente.")
            continue
        classificacao = filmes[filme]["classificacao"]
        if idade >= classificacao:
            agora = datetime.datetime.now()
            print("\n--- INGRESSO ---")
            print(f"Nome: {nome}")
            print(f"Sala: {filmes[filme]['sala']}")
            print(f"Filme: {filmes[filme]['nome']}")
            print(f"Data/Hora da compra: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
            print("Bom filme!")
            break
        else:
            print("Você não tem idade suficiente para assistir a este filme.")
            print("Escolha outro filme.\n")
    except ValueError:
        print("Entrada inválida. Digite um número de 1 a 5.")


"""
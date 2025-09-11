# Lista de itens para fazer compras

itens = [
    "Arroz",
    "Feijão",
    "Macarrão",
    "Leite",
    "Pão",
    "Ovos",
    "Frutas",
    "Legumes",
    "Carne",
    "Café"
]


for i in range (len(itens)):
    print(f"Índice {i}: {itens[i]}.")

try:
    i = int(input("Informe a posição do indice a ser alterado: "))
    if i >= 0 and i < len(itens):
            itens[i] = input("Informe o novo valor: ").capitalize().strip
            print(f"Item alterado com sucesso")
    else:
         print("Indice inválido.")
except Exception as e:
    print (f"Não foi possivel alterar o item da lista. {e}")
finally:
    for i in range (len(itens)):
        print(f"Indice {i}: {itens[i]}.")
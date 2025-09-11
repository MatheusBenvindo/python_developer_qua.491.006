import os  

estados = [
    "São Paulo",
    "Rio de Janeiro",
    "Minas Gerais",
    "Bahia",
    "Paraná",
    "Pernambuco"
]


print ("nomes")

# contador, range = numero de vezes que o for irá executar
for i in range(len(estados)):
    print (f"Índice {i}: {estados[i]}.")

#tratamento de exceção - evita que o programa crashe em caso de inserção inapropriada.
#i = indice

try:
    novo_estado = input("Informe o novo Nome: ").title().strip()
    i = int(input("Informe a posição da lista onde deseja inserir "))
    if i >= 0 and i <len(estados):
        estados.insert(i, novo_estado)
        print ("Cidade inserida com sucesso!")
    else:
        print("Indice inválido")

except Exception as e:
    print(f"Não foi possivel inserir item na lista {e}")

    
finally:
    for i in range(len(estados)):
        print (f"Índice {i}: {estados[i]}.")
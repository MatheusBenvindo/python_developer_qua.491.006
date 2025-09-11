import os  

nomes = ["Matheus",
    "Matthew",
    "Beltrano",
    "Fulano",
    "Ciclano",
    "José"]

for nome in nomes:
    print (nomes)

novo_nome = input("Informe o novo Nome: ").title().strip()
print ("nomes")


nomes.append(novo_nome)

print (nomes)
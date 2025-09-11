#lista 
import os 
nomes = ["Matheus", "Matthew", "Beltrano", "Fulano", "Ciclano", "José"]

#ORDENA A LISTA
nomes.sort(reverse=True) #Inverter Z-A ordem alfabetica.

os.system ('cls')
print (nomes[0])


#Imprime qtd de itens na lista
print('Imprime qtd de itens na lista \n')
print (len(nomes))

# Para saber a posição de algo na lista:
print('Para saber a posição de algo na lista \n')
print(nomes.index("Fulano"))

#para imprimir a lista, conteudo e posições
for nome in nomes:
    print(f"{nome} - {nomes.index(nome)}")
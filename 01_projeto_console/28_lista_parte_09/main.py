import os

nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

#exibição
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print("-"*60)
try:
    i = int(input("Informe o índice que deseja separar: "))
    if i>=0 and i<len(nomes):
        nome_isolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")

        print(f"{nome_isolado} separado com sucesso.")

        #valores atualizados
        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}")
        print("-"*60)

        print(f"Valor isolado da lista: {nome_isolado}")
    else:
        print("Índice inválido!")
except Exception as e:
    print(F"Não foi possivel executar a operação.")


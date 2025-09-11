#ALTERAR VALOR DA CHAVE EXISTENTE
import os 

usuario = dict(nome="Matheus", idade=40, email="matt@gmail.com")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

print ("-"*40)

#usuario informa chave para alterar o valor
chave = input("Informe a chave que deseja alterar: ").lower().strip()

#usuario informa o valor da chave, verificação e aplicação da chave 
if chave in usuario:
    novo_valor = input(f"Informe o novo valor para '{chave}': ")
    usuario[chave] = novo_valor
    print(f"Valor da chave '{chave}' alterado para: {usuario[chave]}")
else:
    print(f"Chave '{chave}' não encontrada no dicionário.")
        
print ("-"*40)

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
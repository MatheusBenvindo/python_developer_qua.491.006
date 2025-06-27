#EXCLUIR VALOR DA CHAVE EXISTENTE
import os 

usuario = dict(nome="Matheus", idade=40, email="matt@gmail.com", profissão="DEV")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
print("-"*40)

#usuário informa chave que deseja excluiir
chave = input("Informe a chave que deseja excluir: ").lower().strip()

if chave in usuario:
    del usuario[chave]
else:
    print(f"Chave '{chave}' não encontrada no dicionário.")
        
print ("-"*40)

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

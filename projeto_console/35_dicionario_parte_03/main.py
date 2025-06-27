#dicionario 

usuario = {
    'nome': "Matheus Ribeiro",
    'idade': 40,
    'email': "matt@gmail.com",
    'profissão': "Dev"
}


for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

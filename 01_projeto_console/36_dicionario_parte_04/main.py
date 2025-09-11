#dicionario

usuario = dict(nome="Matheus", idade=40, email="matt@gmail.com")

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")


print (list(usuario.values()))
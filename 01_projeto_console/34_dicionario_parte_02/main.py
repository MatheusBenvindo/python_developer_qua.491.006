#dicionario 

usuario = {
    'nome': 'Matheus Ribeiro',
    'idade': 40,
    'email': 'matt@gmail.com',
    'profissão': 'Dev'
}

#get = none, vazio pode ser substituido pelo try except para tratamento de erros.
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"email: {usuario.get('email')}")
print(f"Profissão: {usuario.get('profissão')}")

print("-"*60)

# Usando o método values()
print(usuario.values())

print("-"*60)

# Usando um loop for para exibir cada valor
for valor in usuario.values():
    print(valor)

print("-"*60)
# Convertendo para lista
print(list(usuario.values()))

print("-"*60)

# Usando unpacking (desempacotamento)
print(*usuario.values())

print("-"*60)

# Usando list comprehension
[print(valor) for valor in usuario.values()]

print("-"*60)
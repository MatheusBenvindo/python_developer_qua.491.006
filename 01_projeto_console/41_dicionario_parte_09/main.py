usuarios = [{
    'nome': "Fulano",
    'idade': 38,
    'email': "fulano@gmail.com",
},

{
    'nome': "Beltrano",
    'idade': 25,
    'email': "beltrano@gmail.com",
    },
    {
        'nome': "Ciclana",
        'idade': 30,
        'email': "ciclana@gmail.com",
    },
    {
        'nome': "Joana",
        'idade': 22,
        'email': "joana@gmail.com",
    },
    {
        'nome': "Pedro",
        'idade': 41,
        'email': "pedro@gmail.com",
    },
    {
        'nome': "Marina",
        'idade': 29,
        'email': "marina@gmail.com",
    }
]

#exibe os dados
for usuario in usuarios:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")
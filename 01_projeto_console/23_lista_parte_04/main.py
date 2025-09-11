import os  

estados = [
    "São Paulo",
    "Rio de Janeiro",
    "Minas Gerais",
    "Bahia",
    "Paraná",
    "Pernambuco",
    "Ceará",
    "Santa Catarina",
    "Rio Grande do Sul",
    "Goiás",
    "Amazonas",
    "Espírito Santo",
    "Mato Grosso",
    "Maranhão",
    "Paraíba",
    "Alagoas",
    "São Paulo",           # duplicata
    "Bahia",               # duplicata
    "Rio de Janeiro",      # duplicata
    "Ceará"                # duplicata
]


estado_pesquisado = input("Informe o nome da cidade: ").title().strip()

qtd = estados.count(estado_pesquisado)

print (f"{estado_pesquisado} foi encontrado {qtd} vezes na lista.")
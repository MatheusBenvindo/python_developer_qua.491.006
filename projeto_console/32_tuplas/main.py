# Exemplos de tuplas simples em Python, são listas simples já definidas que não poderão ser alteradas.

#pode ser criada, listada, pesquisada entretanto não pode (alterar, incluir, excluir, ordenar)

dias_da_semana = (
    "domingo",
    "segunda_feira",
    "terça_feira",
    "quarta_feira",
    "quinta_feira",
    "sexta_feira",
    "sábado")

for dia in dias_da_semana:
    print (dia)

# Tupla de números inteiros
tupla_numeros = (1, 2, 3, 4, 5)
print("Tupla de números:", tupla_numeros)

# Tupla de strings
tupla_strings = ("maçã", "banana", "laranja")
print("Tupla de strings:", tupla_strings)

# Tupla mista (diferentes tipos de dados)
tupla_mista = (10, "python", 3.14, True)
print("Tupla mista:", tupla_mista)

# Tupla com um único elemento (atenção à vírgula)
tupla_unica = (42,)
print("Tupla com um elemento:", tupla_unica)

# Tupla vazia
tupla_vazia = ()
print("Tupla vazia:", tupla_vazia)
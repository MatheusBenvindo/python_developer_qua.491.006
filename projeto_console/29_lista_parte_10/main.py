#concater lista em uma só variável.

dias_da_semana = [
    "domingo",
    "segunda_feira",
    "terça_feira",
    "quarta_feira",
    "quinta_feira",
    "sexta_feira",
    "sábado"
]

delimitador = ", "

dias_variavel = delimitador.join(dias_da_semana)

print (dias_variavel)
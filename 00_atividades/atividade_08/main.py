"""
#TODO - atividade: Crie um programa que recebe de um professor várias notas de um aluno de 0 a 10 (não importa quantas notas). Ao final do programa, a média das notas deverá ser calculada e informada, e em seguida, o programa irá informar se o aluno:
- Foi aprovado, caso média for maior ou igual a 7
- Ficou de recuperação, caso média for entre 5 e 7
- Foi reprovado, caso média for menor que 5.
"""

import os
lista_notas = []

while True:
    try:
        nota = float(input("Informe uma nota entre 0 e 10 para a soma da média final: ").replace(",", "."))
        if 0 <= nota <= 10:
            print(f"A nota a ser inserida é {nota}")
            confirmar = input("Confirma a nota? (s/n): ").strip().lower()
            if confirmar != 's':
                print("Nota descartada.")
                continue
            lista_notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            continue

        continuar = input("Deseja inserir outra nota? (s/n): ").strip().lower()
        if continuar != 's':
            break
    except Exception as e:
        print("Entrada inválida. Tente novamente.")

if lista_notas:
    for i, n in enumerate(lista_notas, 1):
        print(f"Nota {i}: {n:.2f}")
    media = sum(lista_notas) / len(lista_notas)
    print(f"Média das notas: {media:.2f}")
    if media >= 7:
        print("Aluno aprovado.")
    elif 5 <= media < 7:
        print("Aluno em recuperação.")
    else:
        print("Aluno reprovado.")
else:
    print("Nenhuma nota foi inserida.")
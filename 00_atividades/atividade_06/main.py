"""
# TODO - atividade: Crie um programa em que o usuário informe um ano e o programa exibe todo o calendário do ano informado pelo usuário.
#NOTE - o usuário poderá informar qualquer ano a partir de 1900.
#NOTE - use a biblioteca 'calendar'"""

import os
import calendar

os.system("cls")

ano = int(input("Digite um Ano (a partir de 1900): "))

if ano >= 1900:
    for mes in range(1, 13):
        cal = calendar.TextCalendar()
        print(cal.formatmonth(ano, mes))
else:
    print("Ano inválido. Informe um ano a partir de 1900.")


"""
# TODO - atividade: Crie um programa em que o usuário informe um ano e o programa exibe todo o calendário do ano informado pelo usuário.
#NOTE - o usuário poderá informar qualquer ano a partir de 1900.
#NOTE - use a biblioteca 'calendar'

import os
import calendar

ano = int(input("Digite um Ano (a partir de 1900): "))

if ano >= 1900:
    os.system("cls")
    print(calendar.calendar(ano))
else:
    print("Ano inválido. Informe um ano a partir de 1900.")"""
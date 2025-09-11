aluno = input("Informe o nome do aluno: ")
nota = float(input("Digite a nota do aluno: ").replace(',', '.'))

if nota >= 0 and nota <= 10:
    if nota >= 7:
        print(f"{aluno} - {nota} - APROVADO")
    elif nota >= 5:
        print(f"{aluno} - {nota} - RECUPERAÇÃO")
    else:
        print(f"{aluno} - {nota} - REPROVADO")
else:
    print("Nota inválida,")
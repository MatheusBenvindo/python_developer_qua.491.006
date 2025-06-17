import os
os.system("cls")


#declaração de variáveis
x = float(input("informe o valor de x: ").replace(",","."))
y =float(input("informe o valor de y: ").replace(",","."))

# menu
print(f"{"-"*20} escolha a operação {"-"*20}\n")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

#usuario escolhe a operação desejada

operador = input("Digite o número da operação desejada: ").strip()


# match case
match operador: 
    case "1":
        print(f"A soma dos valores é  {x + y}")
    case "2":
        print(f"A subtração dos valores é  {x - y}")
    case "3":
        print(f"A multiplicação dos valores é  {x * y}")
    case "4":
        print(f"A divisão dos valores é  {x / y}")
    case _: # default
        print("Operação inválida.")

        # fim do programa
        print(" Fim do programa.")
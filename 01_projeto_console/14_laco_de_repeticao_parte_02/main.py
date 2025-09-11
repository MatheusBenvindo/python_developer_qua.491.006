# Loop infinito.
while True:
    # menu.
    print(f"{'-'*20} ESCOLHA A OPERAÇÃO {'-'*20}")
    print("0 - Encerrar o programa.")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print(f"{'-'*60}")

    Operador = input("Informe a opereção desejada: ").strip()

    match Operador:
        case "0":
            print("Programa encerrado.")
            break
        case "1":
            try:
                X = float(input("Informe o valor de X: ").replace(",","."))
                Y = float(input("Informe o valor de Y: ").replace(",","."))

                print(f'{X} + {Y} = {X+Y}.')
            except Exception as e:
                print(f"Não foi possível somar. `{e}.")
            finally:
                continue
        case "2":
            try:
                X = float(input("Informe o valor de X: ").replace(",","."))
                Y = float(input("Informe o valor de Y: ").replace(",","."))

                print(f'{X} - {Y} = {X-Y}.')
            except Exception as e:
                print(f"Não foi possível somar. `{e}.")
            finally:
                continue
        case "3":
            try:
                X = float(input("Informe o valor de X: ").replace(",","."))
                Y = float(input("Informe o valor de Y: ").replace(",","."))

                print(f'{X} * {Y} = {X*Y}.')
            except Exception as e:
                print(f"Não foi possível somar. `{e}.")
            finally:
                continue
        case "4":
            try:
                X = float(input("Informe o valor de X: ").replace(",","."))
                Y = float(input("Informe o valor de Y: ").replace(",","."))

                print(f'{X} / {Y} = {X/Y}.')
            except Exception as e:
                print(f"Não foi possível somar. `{e}.")
            finally:
                continue
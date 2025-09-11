import modulo
"""
# TODO - atividade : Crie um programa que receba do usuário o numero inteiro e calcule o valor da sequência de Fibonnaci.
"""

if __name__ == "__main__":
    while True:
        entrada = input('Informe o número de sequências a ser calculada: ').strip()
        if not entrada:
            print("Entrada em branco. Por favor, informe um número inteiro não negativo.")
            continue
        try:
            n = int(entrada)
            if n < 0:
                print("Por favor, informe um número inteiro não negativo.")
            else:
                print(modulo.fibonacci_recursivo(n))
                break
        except ValueError:
            print("Valor inválido. Por favor, informe um número inteiro não negativo.")
        except Exception as e:
            print(f"Erro {e}.")
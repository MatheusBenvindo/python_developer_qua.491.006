import modulo 
import time

if __name__ == "__main__":
    while True:
        try:
            print (" 1 - Calcular Fatorial")
            print (" 2 - Sair do programa")
            opcao = input("Escolha: ").strip()
            match opcao:
                case "1":
                    n = int(input("Informe um número inteiro: "))
                    print (f"{n}! = {modulo.fatorial(n)}")
                case "2":
                    x = 100000
                    while x > 0:
                        print(f"Programa encerrado em {x}.")
                        time.sleep(1)
                        x -= 1
                    break
                case "_":
                    print ("Opção inválida")
                    continue
        except Exception as e:
            print (F"ERRO {e}")
            continue
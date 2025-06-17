import os
import time
os.system("cls")

try: # Entrada de dados.
    Numero = int(input("Informe um número inteiro: "))

    # Saída de dados.
    while Numero >= 0:
        os.system("cls")
        print(f"{Numero} ...")
        time.sleep(1)
        os.system('cls')
        Numero -= 1         
    
except Exception as e:
    print (f"Não foi possivel executar a contagem. {e}")

finally:
    os.system("cls")
    print ("BOOOM!")

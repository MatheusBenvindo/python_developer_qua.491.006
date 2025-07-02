import os

#entrada de dados.
while True:
    try:
        arquivo = input("Qual arquivo você deseja abrir?\narquivo.txt\nmsg.txt\nnew.txt\ntexto.txt\n").strip().lower()
        
        with open (f"{arquivo}.txt", "r", encoding="utf-8") as f:
            arquivo_aberto = f.read()

        os.system("cls")
        print (arquivo_aberto)

        while True:
            prosseguir = input(f"Deseja abrir outro arquivo?").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print ("Opção inválida")
                continue
        match prosseguir:
            case "s":
                continue
            case "n":
                break
            case _:
                print("Opção inválida")
    except Exception as e:
        print(f"Não foi possível ler o arquivo. {e}")
        continue

# #leitura de arquivo
# # O arquivo "texto.txt" deve estar no caminho especificado:
# # C:\Users\ead\PYTHON DEVELOPER QUA.491.006\python_developer_qua.491.006\manipulacao_arquivos

# # Caminho absoluto para o arquivo texto.txt
# caminho_arquivo = r"C:\Users\ead\PYTHON DEVELOPER QUA.491.006\python_developer_qua.491.006\manipulacao_arquivos\texto.txt"

# with open(caminho_arquivo, "r", encoding="utf-8") as f:
#     texto = f.read()

# #saida de dados

# print(texto)
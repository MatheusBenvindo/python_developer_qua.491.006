# gravar arquivo com dados.
import os

while True:
    try:
        novo_texto = input("Digite o texto:\n")
        nome_arquivo = input("Informe o nome do arquivo. (Sem extensão): ").strip().lower()
        with open(f"44_manipular_arquivo_parte_03/{nome_arquivo}.txt", "w", encoding="utf-8") as f:
            f.write(novo_texto)
        os.system("cls")
        print(f"{nome_arquivo}.txt gravado com sucesso")
        while True:
            prosseguir = input(f"Deseja abrir outro arquivo?").strip().lower()
            if prosseguir == "s" or prosseguir == "n":
                break
            else:
                print("Opção inválida")
                continue
        match prosseguir:
            case "s":
                continue
            case "n":
                break
            case _:
                pass
    except Exception as e:
        print(f"Não foi possivel gravar arquivo. {e}")
        continue
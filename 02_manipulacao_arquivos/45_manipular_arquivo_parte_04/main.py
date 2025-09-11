import os

arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()

try:
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)

    novo_texto = input("Digite o texto: \n")

    with open(f"{arquivo}.txt", "w", encoding="utf-8") as f:
        texto = f.write()
    print(novo_texto)

    
except Exception as e:
    print(f"Não foi possivel atualizar arquivo. {e}")

import os

arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()

try:
    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    print(texto)

    novo_texto = input("Digite o texto: \n")

    # Abre o arquivo em modo de adição ("a") para não sobrescrever
    with open(f"{arquivo}.txt", "a", encoding="utf-8") as f:
        f.write(novo_texto + "\n") 

    print("Texto adicionado com sucesso!")

    with open(f"{arquivo}.txt", "r", encoding="utf-8") as f:
        texto_final = f.read()
    print(texto_final)

except Exception as e:
    print(f"Não foi possivel atualizar arquivo. {e}")

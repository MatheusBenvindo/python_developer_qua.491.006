from deep_translator import GoogleTranslator
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print("=== Tradutor de Texto ===")
    print("1 - Traduzir texto")
    print("2 - Sair do programa")
    print("========================")

def traduzir_texto(tradutor):
    texto_original = input("Digite o texto que deseja traduzir: ").strip()
    if not texto_original:
        print("Nenhum texto informado para tradução.")
        return
    
    limpar_tela()  

    try:
        texto_traduzido = tradutor.translate(texto_original)
        print("\nTexto traduzido:\n" + texto_traduzido + "\n")
    except Exception as e:
        print(f"Erro ao traduzir o texto: {e}")


def main():
    tradutor = GoogleTranslator(source="auto", target="pt")


    while True:
        mostrar_menu()
        opcao = input("Informe a opção desejada: ").strip()
        limpar_tela()

        match opcao:
            case "1":
                traduzir_texto(tradutor)
            case "2":
                print("Programa encerrado. Até logo!")
                break
            case _:
                print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()

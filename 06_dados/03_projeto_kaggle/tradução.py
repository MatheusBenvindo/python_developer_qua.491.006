import json
import os
from deep_translator import GoogleTranslator

def traduzir_notebook_markdown(entrada, saida, target="pt"):
    if not entrada.endswith(".ipynb"):
        entrada += ".ipynb"
    if not saida.endswith(".ipynb"):
        saida += ".ipynb"

    if not os.path.exists(entrada):
        print(f"❌ Arquivo não encontrado: {entrada}")
        return

    with open(entrada, "r", encoding="utf-8") as f:
        notebook = json.load(f)

    tradutor = GoogleTranslator(source="auto", target=target)

    for i, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") == "markdown":
            print(f"📝 Traduzindo célula Markdown {i}")
            novo_source = []
            for linha in cell.get("source", []):
                try:
                    if linha.strip():
                        print(f"   🔤 Original: {linha.strip()}")
                        traducao = tradutor.translate(linha)
                        print(f"   ✅ Traduzido: {traducao}")
                        novo_source.append(traducao + "\n")
                    else:
                        novo_source.append("\n")
                except Exception as e:
                    print(f"⚠️ Erro ao traduzir linha: {e}")
                    novo_source.append(linha)
            cell["source"] = novo_source

    with open(saida, "w", encoding="utf-8") as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)

    print(f"✅ Tradução concluída! Arquivo salvo em: {saida}")

if __name__ == "__main__":
    traduzir_notebook_markdown(
        "C:/Users/ead/python_developer_qua.491.006/dados/03_projeto_kaggle/serial-murder-analysis.ipynb",
        "C:/Users/ead/python_developer_qua.491.006/dados/03_projeto_kaggle/serial-murder-analysis-traduzido.ipynb"
    )

import os

#leitura de arquivo
# O arquivo "texto.txt" deve estar no caminho especificado:
# C:\Users\ead\PYTHON DEVELOPER QUA.491.006\python_developer_qua.491.006\manipulacao_arquivos

# Caminho absoluto para o arquivo texto.txt
caminho_arquivo = r"C:\Users\ead\PYTHON DEVELOPER QUA.491.006\python_developer_qua.491.006\manipulacao_arquivos\texto.txt"

with open(caminho_arquivo, "r", encoding="utf-8") as f:
    texto = f.read()

#saida de dados

print(texto)
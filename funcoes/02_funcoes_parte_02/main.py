def exibir_mensagem(nome):

    return f"Seja bem-vindo, {nome}"


nome = input("Informe seu nome").strip().title()

print (exibir_mensagem(nome))

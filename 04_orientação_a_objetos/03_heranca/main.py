import classes as c
import os
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # Instância as classes
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # Input do usuário
    print("Entre com os dados do usuário\n")

    usuario.nome = input("Nome: ").strip().title()
    usuario.cpf = input("CPF: ").strip()
    usuario.telefone = input("Telefone: ").strip()
    usuario.endereco = input("Endereço: ").strip().title()
    limpar()

    # Input da empresa
    print("Entre com os dados da empresa\n")

    empresa.nome_fantasia = input("Nome fantasia: ").strip().title()
    empresa.cnpj = input("CNPJ: ").strip()
    empresa.telefone = input("Telefone: ").strip()
    empresa.endereco = input("Endereço: ").strip().title()
    limpar()

    # Output
    limpar()
    print("Dados do usuário:")
    usuario.exibir_dados()
    print("\nDados da empresa:")
    empresa.exibir_dados()

if __name__ == "__main__":
    main()
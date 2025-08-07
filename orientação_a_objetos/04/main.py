import classes as c
import os

# Limpar a tela
limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # Instancia as classes com valores vazios
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nomefantasia="", cnpj="", telefone="", endereco="")

    # Entrada de dados do usuário
    print("Entre com os dados do usuário\n")
    usuario.nome = input("Nome: ").strip().title()
    usuario.cpf = input("CPF: ").strip()
    usuario.telefone = input("Telefone: ").strip()
    usuario.endereco = input("Endereço: ").strip().title()
    limpar()

    # Entrada de dados da empresa
    print("Entre com os dados da empresa\n")
    empresa.nomefantasia = input("Nome fantasia: ").strip().title()
    empresa.cnpj = input("CNPJ: ").strip()
    empresa.telefone = input("Telefone: ").strip()
    empresa.endereco = input("Endereço: ").strip().title()
    limpar()

    # Saída dos dados
    print("=== Dados do Usuário ===")
    print(f"Nome: {usuario.nome}")
    print(f"CPF: {usuario.cpf}")
    print(f"Telefone: {usuario.telefone}")
    print(f"Endereço: {usuario.endereco}")

    print("\n=== Dados da Empresa ===")
    print(f"Nome Fantasia: {empresa.nomefantasia}")
    print(f"CNPJ: {empresa.cnpj}")
    print(f"Telefone: {empresa.telefone}")
    print(f"Endereço: {empresa.endereco}")

if __name__ == "__main__":
    main()


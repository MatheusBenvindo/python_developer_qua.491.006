import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="", idade="")



    #inputs 
    usuario.nome = input("Informe seu nome: ").strip().title()
    usuario.idade = int("Informe sua idade: ").strip().title()

    print(usuario)
if __name__ == "__main__":
    main()
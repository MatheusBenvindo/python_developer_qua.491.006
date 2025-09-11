from classes import Dono, Carro

def main():
    # Criando um dono
    dono1 = Dono("Ana Oliveira", "123.456.789-00", "Feminino", "Rua das Flores, 101")

    # o dono é parte da criação do carro
    carro1 = Carro("Volkswagen Golf", "ABC-1234", "Azul", dono1)

    # Exibir os dados completos 
    print("Informações do Carro:")
    print(carro1.exibir_dados_carro())

if __name__ == "__main__":
    main()

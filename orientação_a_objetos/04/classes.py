# Encapsulamento

# Superclasse ou classe-pai
class Pessoa:
    def __init__(self, telefone, endereco):
        self.__telefone = telefone
        self.__endereco = endereco

    # getter telefone
    @property
    def telefone(self):
        return self.__telefone

    # setter telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    # getter endereco
    @property
    def endereco(self):
        return self.__endereco

    # setter endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

class PessoaFisica(Pessoa):
    def __init__(self, nome, cpf, telefone, endereco):
        self.__nome = nome
        self.__cpf = cpf
        super().__init__(telefone, endereco)

    # getter nome
    @property
    def nome(self):
        return self.__nome

    # setter nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # getter cpf
    @property
    def cpf(self):
        return self.__cpf

    # setter cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

class PessoaJuridica(Pessoa):
    def __init__(self, nomefantasia, cnpj, telefone, endereco):
        self.__nomefantasia = nomefantasia
        self.__cnpj = cnpj
        super().__init__(telefone, endereco)

    # getter nomefantasia
    @property
    def nomefantasia(self):
        return self.__nomefantasia

    # setter nomefantasia
    @nomefantasia.setter
    def nomefantasia(self, nomefantasia):
        self.__nomefantasia = nomefantasia

    # getter cnpj
    @property
    def cnpj(self):
        return self.__cnpj

    # setter cnpj
    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj
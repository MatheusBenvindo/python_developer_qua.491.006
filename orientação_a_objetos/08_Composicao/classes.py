# Classe Dono representa um dono de carro
class Dono:
    def __init__(self, nome, cpf, sexo, endereco):
        self.__nome = nome
        self.__cpf = cpf 
        self.__sexo = sexo
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    def exibir_dados_dono(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nSexo: {self.sexo}\nEndereço: {self.endereco}"

# Classe Carro contém (ou seja, é composta por) um objeto da classe Dono
class Carro:
    def __init__(self, modelo, placa, cor, dono):
        self.__modelo = modelo
        self.__placa = placa
        self.__cor = cor
        self.dono = dono  # Aqui é composição!

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        if isinstance(dono, Dono):
            self.__dono = dono
        else:
            raise TypeError("dono deve ser uma instância da classe Dono")

    def exibir_dados_carro(self):
        return f"""Modelo: {self.modelo}
Placa: {self.placa}
Cor: {self.cor}
Dono:
{self.dono.exibir_dados_dono()}
"""


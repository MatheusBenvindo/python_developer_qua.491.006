#simplifica a forma de trabalho com classes - ex operador ternário
from dataclasses import dataclass

@dataclass
class Pessoa:
    #atributos
    nome : str
    idade: int

    def __str__(self):
        return f"Nome: {self.nome}"

    def __len__(self):
        return self.idade
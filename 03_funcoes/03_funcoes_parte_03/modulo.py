#funcoes
import os
def area_quadrado(L):
    a = L**2
    return a

def area_retangulo(B, H):
    a = B*H
    return a

def area_triangulo (B, H):
    a = (B*H)/2
    return a

def limpa_tela():
    os.system("cls" if os.name == "nt" else "clear")
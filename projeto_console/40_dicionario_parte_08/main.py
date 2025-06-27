import os

chaves = ("Nome", "Idade", "Email", "Telefone", "Profissão")

usuario = {
    chaves[0]: "Matheus Ribeiro",
    chaves[1]: 80,
    chaves[2]: "matt@gmail.com",
    chaves[3]: "1140028922",
    chaves[4]: "programador"
}

for chave in usuario:
    print(f"{chave}: {usuario.get(chave)}")
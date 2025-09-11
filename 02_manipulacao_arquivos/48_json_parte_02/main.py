import json
import os 


pessoa = {
}

try:
    #usuario informa o arquivo
    arquivo = input(f"Informe o arquivo (sem extensão)").strip().lower()
    #le json e desserializa para dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f) 
    
    # Lista de campos e funções de conversão
    campos = [
        ("nome", str, "Informe o nome: ", lambda x: x.strip().title()),
        ("idade", int, "Informe sua idade: ", int),
        ("cpf", str, "Informe o cpf: ", lambda x: x.strip()),
        ("rg", str, "Informe o rg: ", lambda x: x.strip()),
        ("data_nasc", str, "Informe a data de nascimento: ", lambda x: x.strip()),
        ("sexo", str, "Informe o gênero: ", lambda x: x.strip()),
        ("signo", str, "Informe o signo: ", lambda x: x.strip().capitalize()),
        ("mae", str, "Informe o nome da mãe: ", lambda x: x.strip().title()),
        ("pai", str, "Informe o nome do pai: ", lambda x: x.strip().title()),
        ("email", str, "Informe o email: ", lambda x: x.strip().lower()),
        ("senha", str, "Informe a senha: ", lambda x: x.strip()),
        ("cep", str, "Informe o cep: ", lambda x: x.strip().lower()),
        ("endereco", str, "Informe o endereço: ", lambda x: x.strip().title()),
        ("numero", int, "Informe o número: ", int),
        ("bairro", str, "Informe o bairro: ", lambda x: x.strip().title()),
        ("cidade", str, "Informe a cidade: ", lambda x: x.strip().title()),
        ("estado", str, "Informe o estado: ", lambda x: x.strip().upper()),
        ("telefone_fixo", str, "Informe o telefone fixo: ", lambda x: x.strip()),
        ("celular", str, "Informe o celular: ", lambda x: x.strip()),
        ("altura", float, "Informe a altura (ex: 1.75): ", float),
        ("peso", float, "Informe o peso (ex: 70.5): ", float),
        ("tipo_sanguineo", str, "Informe o tipo sanguíneo: ", lambda x: x.strip().upper()),
        ("cor", str, "Informe a cor: ", lambda x: x.strip()),
    ]

    for campo, tipo, mensagem, conversao in campos:
        valor = input(mensagem)
        pessoa[campo] = conversao(valor)

    lista.append(pessoa)

    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f) 

    print(f'{'-'*20} LISTA DE PESSOAS {'-'*20}')
    for pessoa in lista:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print ('-'*40)
    
except Exception as e:
    print ("Não foi possivel inserir pessoa")
    
"""
import json
import os 


pessoa = {
}

try:
    #usuario informa o arquivo
    arquivo = input(f"Informe o arquivo (sem extensão)").strip().lower()
    #le json e desserializa para dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        lista = json.load(f) 
    
    #usuario informa os dados da nova pessoa:
    pessoa['nome'] = input("Informe o nome: ").strip().title()
    pessoa['idade'] = int(input("Informe sua idade: "))
    pessoa['cpf'] = input("Informe o cpf: ").strip()
    pessoa['rg'] = input("Informe o rg: ").strip()
    pessoa['data_nasc'] = input("Informe a data de nascimento: ").strip()
    pessoa['sexo'] = input("Informe o gênero: ").strip()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("Informe o nome da mãe: ").strip().title()
    pessoa['pai'] = input("Informe o nome do pai: ").strip().title()
    pessoa['email'] = input("Informe o email: ").strip().lower()
    pessoa['senha'] = input("Informe a senha: ").strip()
    pessoa['cep'] = input("Informe o cep: ").strip().lower()
    pessoa['endereco'] = input("Informe o endereço: ").strip().title()
    pessoa['numero'] = int(input("Informe o número: "))
    pessoa['bairro'] = input("Informe o bairro: ").strip().title()
    pessoa['cidade'] = input("Informe a cidade: ").strip().title()
    pessoa['estado'] = input("Informe o estado: ").strip().upper()
    pessoa['telefone_fixo'] = input("Informe o telefone fixo: ").strip()
    pessoa['celular'] = input("Informe o celular: ").strip()
    pessoa['altura'] = float(input("Informe a altura (ex: 1.75): "))
    pessoa['peso'] = float(input("Informe o peso (ex: 70.5): "))
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguíneo: ").strip().upper()
    pessoa['cor'] = input("Informe a cor: ").strip().lower()
    
except Exception as e:
    print ("Não foi possivel inserir pessoa")"""
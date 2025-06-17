import os
os.system("cls")


"""
# TODO -
# ATIVIDADE 02
crie um programa que receba usuario, o nome,o peso em kg,
 e a altura em metros,e calcule o
IMC (Indice de Massa Corporal).
O programa deve mostrar o valor do Imc arredondado para 2 casas
 decimais ,e mostrar o diagnostico do usuario com base nos seguintes valores:
 - Caso o IMC  seja menor que 18.5 , = "abaixo do seu peso"
 - caso o IMC seja maior ou igual a 18.5 e menor que 25 = " peso ideal"
 - caso o IMC seja maior ou igual a 25 e menor que 30 = "acima do peso"
 - caso o IMC seja maior ou igual a 30 e menor que 35 = "obeso"
 - caso o IMC seja maior ou igual a 35 e menor que 40 = "obesidade nível 2"
 - caso o IMC seja maior ou igual a 40 = "obesidade morbida"

 # NOTE - O usuario deverá informar o encerramento do programa ,ou seja,ele poderá repetir
 o calculo quantas vezes quiser.



"""

#laço de repetição
while True:
    try:
        #entrada de dados
        nome = input("Informe o seu nome: ").title().strip()
        peso = float(input("Informe o seu peso em kg: ").replace(",", "."))
        altura = float(input("Informe a sua altura em metros: ").replace(",", "."))
        imc = peso / (altura ** 2)
        if imc < 18.5:
            diagnostico = "Abaixo do peso"
        elif 18.5 <= imc < 25:
            diagnostico = "Peso ideal"
        elif 25 <= imc < 30:
            diagnostico = "Acima do peso"
        elif 30 <= imc < 35:
            diagnostico = "Obeso"
        elif 35 <= imc < 40:
            diagnostico = "Obesidade nível 2"
        else:
            diagnostico = "Obesidade mórbida"
        print(f"{nome}, seu IMC é {imc:.2f}. Diagnóstico: {diagnostico}")
        
        while True:
            opcao = input("Deseja calcular novamente? (s/n): ").lower().strip()
            if opcao == "s" or opcao == "n":
                break
            else:
                print ("Opção inválida.")
                continue
        match opcao:
            case "s":
                continue
            case "n":
                break

    except Exception as e:
        print(f"Não foi possivel executar operação.")

        continue

    # FIM DO PROGRAMA
print("Programa encerrado.")
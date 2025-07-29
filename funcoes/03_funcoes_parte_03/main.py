#importando arquivos da função
import modulo as m

def limpa():
    pass

#algoritmo principal. bloqueia a importação do main
if __name__ == "__main__":
    while True:
        print("1 - Calcular quadrado.")
        print("2 - Calcular retângulo.")
        print("3 - Calcular triângulo.")
        print("4 - Sair do programa.")
        opcao = input("Informe a opção desejada: ").strip()
        m.limpa_tela
        
        try:
            match opcao:
                case "1":
                    try:
                        print("Você escolheu calcular quadrado.")
                        L = int(input("Informe o lado do quadrado"))
                        a = m.area_quadrado(L)
                        print(f"Área do quadrado: {a}.")
                    except Exception as e:
                        print(f"Erro. {e}")
                    finally:
                        continue
                case "2":
                    try:
                        B = int(input("Informe a base do retângulo: "))
                        H = int(input("Informe a altura do retângulo: "))
                        a = m.area_retangulo(B,H)

                        print(f"Área do retângulo {a}")
                    except Exception as e:
                        print(f"Erro. {e}")
                    finally:
                        continue
                case "3":
                    try:
                        B = int(input("Informe a base do triângulo"))
                        H = int(input("Informe a altura do triângulo"))
                        a = m.area_triangulo(B,H)

                        print (f"Área do triângulo {a}")
                    except Exception as e:
                        print(f"Erro {e}")
                    finally:
                        continue   
                case "4":
                    print("Saindo do programa.")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    continue
                    
        except Exception as e:
            print ("Não foi possivel fazer a operação")
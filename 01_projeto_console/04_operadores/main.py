import os
os.system("cls")
# declaracao de variaveis
x = 5 
y = 2
#result =  x- y # Convertendo para inteiro antes da subtração e depois para string para concatenar

#convertendo números para string
#x = str(x)
#y = str(y)
#result = str(result)


# operadores 
#print("Soma dos valores de:", x, "e",  x+y, ".") 
#print("Subtração dos valores de: " +  x  +  " e "  + y +  " é " + result +  ".")


# operações 
soma = x + y
Subtracao = x - y
Multiplicacao = x * y
Divisao = x / y
resto = x % y
potencia = x ** y


print("A soma de {} e {} é {}.".format(x,y, soma))
print(f"A subtração de {x} e {y} é {Subtracao}.")
print(f"A multiplicação de {x} e {y} é {Multiplicacao}.")
print(f"A divisão de {x} e {y} é {Divisao}.")  
print(f"O resto da divisão de {x} e {y} é {resto}.")
print(f"{x} elevado a {y} é {potencia}.")


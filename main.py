#quando eu preciso que o programa entenda que é uma palavra, eu coloco entre aspas ""    
# str significa string

import math

nome = "Vitim"
idade = 29.10
professor = True

a = 1
b = -5
c = 6
delta = (b*b - 4*a*c)

if delta < 0:
    print("Não existe raiz real")
    
elif delta == 0:
    x = -b / (2*a)
    print(f"A raiz da equação é: {x}")



def equacao2grau(a, b, c):
    x1 = -b +math.sqrt(delta) / (2*a)
    return x1

def equacao2grau2(a, b, c):
    x2 = -b - math.sqrt(delta) / (2*a)
    return x2

print(f"O resultado do x1 é:{equacao2grau(a, b, c)}")
print(f"O resultado do x2 é:{equacao2grau2(a, b, c)}")
#Para importar valores de variaveis e funçoes dentro do phyton devemos utilizar chaves {}



print(type(nome).__name__)

print(type(idade).__name__)

print(type(professor).__name__)
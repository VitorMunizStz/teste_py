#Quando eu preciso que o programa entenda que é uma palavra eu coloco entre aspas

from math import sqrt


nome = "Vitim"
vitor = True
print(type(vitor))

a = 5
b = 6
c = 7

def equacao2grau(a, b, c):
    x1 = -b + sqrt(b*b - 4*a*c) / (2*a)
    return x1

print(f"O resultado de x1 é: {equacao2grau(a, b, c)}")
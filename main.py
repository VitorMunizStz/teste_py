#Quando eu preciso que o programa entenda que é uma palavra eu coloco entre aspas

from math import sqrt


nome = "Vitim"
vitor = True
print(type(vitor))

a = 1
b = -5
c = 6
delta = (b**2 - 4*a*c)

if delta < 0:
    print("Não existe raiz real")
else:
    def equacao2grau(a, b, c):
        x1 = -b + sqrt(delta) / (2*a)
        return x1

    def equacao2grau2(a, b, c):
        x2 = -b - sqrt(delta) / (2*a)
        return x2

print(f"O resultado de x1 é: {equacao2grau(a, b, c)}")
print(f"O resultado de x2 é: {equacao2grau2(a, b, c)}")
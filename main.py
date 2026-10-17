#Quando eu preciso que o programa entenda que é uma palavra eu coloco entre aspas

from math import sqrt


nome = "Vitim"
vitor = True
print(type(vitor))

def equacacao2grau(a, b, c):
    x1 = -b + sqrt(b*b - 4*a*c) / (2*a)
    x2 = -b - sqrt(b*b - 4*a*c) / (2*a)
    return x1, x2
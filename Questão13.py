'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

base = eval(input("Digite um número: "))
expoente = eval(input("Digite um número: "))
x = 1
resultado = 1

while (x <= expoente):
    resultado = resultado * base
    x = x + 1

print("")
print("O primeiro número: ",base)
print("O segundo número: ",expoente)
print(base, "elevado a", expoente, "é igual a: ",resultado)

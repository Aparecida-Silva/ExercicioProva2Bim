'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números
pares e a quantidade de números impares.
'''

numero = int(input("Digite um valor inteiro: "))
par=0 
impar=0 
cont = 0

while cont <= 9:
    if (numero % 2 == 0):
     	par = par + 1
    else:
     	impar = impar + 1
    if (cont < 9):
        numero = int(input("Digite um número inteiro: "))
    cont = cont + 1

print("")
print("Obrigado(a)! Você informou 10 números inteiros")
print("Número de impares: ", impar)
print("Número de pares: ", par)

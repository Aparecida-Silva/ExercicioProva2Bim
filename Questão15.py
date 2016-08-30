'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa
capaz de gerar a série até o n−ésimo termo.
'''

numero = int(input("Digite um número: "))

sequencia = 1
a = 0
b = 1
print(b)

while (sequencia < numero):
	c = a + b
	print(c)
	a = b
	b = c
	sequencia = sequencia + 1
	




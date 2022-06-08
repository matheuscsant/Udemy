'''
10 - Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
'''

soma = 0
seq = 0
resultado = 0
for seq in range(0, 50):
    soma = soma + 2
    resultado = soma + resultado

print(resultado)

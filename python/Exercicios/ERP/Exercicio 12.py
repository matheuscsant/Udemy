'''
12 - Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente
'''

print(f'Digite um número inteiro positivo.')

res = int(input(f'R: '))

seq = 0

for seq in range(res, -1, -1):

    print(seq)
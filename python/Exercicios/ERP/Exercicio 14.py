'''
14 - Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente
'''

print(f'Digite um número inteiro positivo par')
res = int(input(f'R: '))

validador = res % 2
seq = 0

if validador == 0:
    for seq in range(res, -2, -2):
        print(seq)
else:
    print(f'Este número não é par')
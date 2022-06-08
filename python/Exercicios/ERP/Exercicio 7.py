'''
7 - Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média
'''

seq = 0
soma = 0
loop = 0
for i in range(0, 10):
    print(f'Digite o número para ser feita a média')
    num = int(input(f'R: '))
    if num > 0:
        soma = num + soma
        loop = loop + 1
    else:
        print(f'\nNúmero não considerado por ser negativo.')

media = soma / loop
print(f'A média de seus números será de: {media:.2f}.')

'''
6 - Faça um programa que leia 10 números inteiros e imprima sua média
'''

seq = 0
soma = 0
for seq in range(0, 10):
    print(f'Digite o número para calcular a média')
    num = int(input(f'R: '))
    soma = num + soma
media = soma / 10
print(f'\nSua média é: {media}')

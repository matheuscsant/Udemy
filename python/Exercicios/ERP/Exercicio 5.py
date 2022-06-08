'''
5 - Faça um programa que peça ao usuário para digitar 10 valores e some-os
'''

seq = 0
total = 0

for seq in range(0, 10):
    print(f'Digite o número que deseja somar')
    num = int(input(f'R: '))
    total = num + total
    print(f'\nA soma dos seus números foi de: {total}.')
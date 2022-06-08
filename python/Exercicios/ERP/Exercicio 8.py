'''
8 - Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
'''

import math
seq = 0
i = 0
menor = math.inf #Apenas valores iniciais
maior = 0
for seq in range(0, 10):
    print(f'\nDigite o número para comparação')
    num = int(input(f'R: '))
    
    if num > maior:
        maior = num
    elif num < menor: #Primeiro loop compara com o infinito
        menor = num   #Em seguida substitui o infinito pelo menos número informado pelo usuário

print(f'O maior valor encontrado foi {maior} e o menor foi {menor}')
'''
9 - Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares
'''

print(f'Digite um número inteiro inteiro e positivo (número natural)')
num = int(input(f'R: '))

seq = 0
if num >= 0:
    sobra = num % 2
    if sobra == 1:
        for seq in range(0, 10):
            num = num + 2
            print(f'Segue a sequência de números: {num}.')
    else:
        num = num + 1
        for seq in range(0, 10):
            print(f'Segue a sequência de números: {num}.')
            num = num + 2

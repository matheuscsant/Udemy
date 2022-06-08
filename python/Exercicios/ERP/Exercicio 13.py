'''
13 - Faça um programa que leia um número inteiro positov par N e imprima todos os números pares de 0 até N em ordem crescente.
'''
print(f'Digite um número inteiro positivo par.')

res = int(input(f'R: '))

seq = 0

validar = res % 2

if validar == 0:
    for seq in range(0, res + 2, 2):
        print(seq)
else:
    print(f'Este número não é par')
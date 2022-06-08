'''
15 - Faça um programa que leia um número inteiro positivo impar N e 
    imprima todos os números impares de 1 até N em ordem crescente
'''

print(f'Digite um número inteiro positivo impar')
res = int(input(f'R: '))

validador = res % 2
seq = 0

if validador == 1:
    for seq in range (1, res + 2, 2):
        print(seq)
else:
    print(f'Este número não é impar')

'''
17 - Faça um programa que leia um número inteiro positivo N 
    e calcule a soma dos n primeiros números naturais.
'''

print(f'Digite um número inteiro positivo')
res = int(input(f'R: '))

seq = 0
resultado = 0

for seq in range(0, res + 1, 1):
    resultado = seq + resultado
print(f'O resultado foi de {resultado:.2f}')
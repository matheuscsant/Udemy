import math

print(f'\nDigite um número positivo.')
num1 = float(input(f'\nR: '))

if num1 >= 0:
    print(f'\nO quadrado do seu número é {num1 ** 2} e sua raiz é {math.sqrt(num1)}.\n')
else:
    print(f'\nNão entendi o que você quis dizer, execute novamente.\n')
    
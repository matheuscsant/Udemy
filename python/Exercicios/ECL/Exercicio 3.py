import math

print(f'\nDigite um número, se ele for positvo, você vera a raiz, do contrário verá o seu quadrado.')
num1 = float(input('\nR: '))

if num1 >= 0:
    print(f'\nA raiz do seu número é {math.sqrt(num1)}\n')
else:
    print(f'\nO quadrado do seu número é {num1 ** 2}\n')
    
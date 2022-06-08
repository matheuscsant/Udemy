print(f'\nDigite um número.')
num1 = float(input(f'\nR: '))

newn1 = num1 % 2

if newn1 > 0:
    print(f'\nSeu número é impar.\n')
else:
    print(f'\nSeu número é par.\n')

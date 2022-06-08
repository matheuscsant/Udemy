print(f'\nDigite um número.')
num1 = float(input(f'\nR: '))

print(f'\nDigite outro número.')
num2 = float(input(f'\nR: '))

if num1 > num2:
    print(f'\nO {num1} é maior que {num2} por {num1 - num2} de diferença.\n')
else:
    print(f'\nO {num2} é maior que {num1} por {num2 - num1} de diferença.\n')

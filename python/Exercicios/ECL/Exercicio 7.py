print(f'\nDigite um número.')
num1 = float(input(f'\nR: '))

print(f'\nDigite outro número.')
num2 = float(input(f'\nR: '))

if num1 > num2:
    print(f'\n{num1} é maior que {num2};\n')

elif num1 == num2 or num2 == num1:
    print(f'\nAmbos os números são iguais.\n')

else:
    print(f'\n{num2} é maior que {num1};\n')

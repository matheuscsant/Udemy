
print(f'\nDigite o comprimeiro de um lado do triângulo')
lado1 = float(input('R: '))

print(f'\nDigite o comprimeiro de outro lado do triângulo')
lado2 = float(input('R: '))

print(f'\nDigite o comprimeiro de outro lado do triângulo')
lado3 = float(input('R: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado3:
    if lado1 == lado2 == lado3:
        print(f'Seu triângulo é equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print(f'Seu triângulo é isósceles.')
    else:
        print(f'Seu triângulho é escaleno.')
else:
    print(f'Seus dados não correspondem a um triângulo.')

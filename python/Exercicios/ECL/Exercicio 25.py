import math

print(f'Digite o valor de a')
valor_a = float(input('R: '))

print(f'\nDigite o valor de b')
valor_b = float(input('R: '))

print(f'\nDigite o valor de c')
valor_c = float(input('R: '))

delta = (valor_b ** 2) - 4 * valor_a * valor_c

if valor_a > 0:
    if delta < 0:
        print(f'\nNão existe raiz')
    elif delta == 0:
        x_positivo = (-valor_b + math.sqrt(delta)) / 2 * valor_a
        print(f'\nRaiz única: {x_positivo}')
    elif delta >= 0:
        x_positivo = (-valor_b + math.sqrt(delta)) / 2 * valor_a
        x_negativo = (-valor_b - math.sqrt(delta)) / 2 * valor_a
        print(f'\nDuas raizes: {x_positivo, x_negativo}')
else:
    print(f'O valor de A precisa ser maior que 0')

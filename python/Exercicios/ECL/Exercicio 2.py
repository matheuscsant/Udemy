import  math

print(f'\nDigite um número (Lembre-se ele precisa ser positivo).')
num1 = int(input(f'\nR:'))

if num1 >= 0:
    print(f'\nA raiz do seu número é {math.sqrt(num1)}\n')
else:
    print(f'\nNúmero inválido, execute novamente.\n')

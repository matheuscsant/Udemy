import math

print(f'Digite um número')
num = int(input('\nR: '))

if num >= 0:
    
    result = math.log(num)
    
    print(f'\nO log de seu número é: {result}')

else:
    
    print(f'\nNúmero inválido.')
    
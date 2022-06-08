
print(f'Digite um número')
num = int(input('\nR: '))

soma = 0

if num > 0:
    numero = str(num)
    for x in numero:
        soma = int(x) + soma
    print(f'A soma dos digitos do seu número é: {soma}')
else:
    print(f'Número inválido')

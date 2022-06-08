print(f'Digite um número')
num1 = int(input(f'R: '))

print(f'\nDigite outro número')
num2 = int(input(f'R: '))

print(f'\nDigite outro número')
num3 = int(input(f'R: '))

print(f'\nQual sua escolha de média?\n'
      f'[1] Geométrica\n'
      f'[2] Ponderada\n'
      f'[3] Harmônica\n'
      f'[4] Aritmética')
res = int(input(f'R: '))

if res > 0:
    if res == 1:
        raiz = num1 * num2 * num3
        result = raiz ** (1/3)
        print(f'Seu resultado foi {result:.2f}')
    elif res == 2:
        result = (num1 + (2 * num2) + (3 * num3)) / 6
        print(f'Seu resultado foi {result:.2f}')
    elif res == 3:
        result = 1 / ((1 / num1) + (1 / num2) + (1 / num3))
        print(f'Seu resultado foi {result:.2f}')
    elif res == 4:
        result = (num1 + num2 + num3) / 3
        print(f'Seu resultado foi {result:.2f}')
    else:
        print(f'Opção inválida, tente novamente.')
else:
    print(f'Algum(uns) de seus números não é inteiro e positivo, tente novamente.')

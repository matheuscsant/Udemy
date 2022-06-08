print(f'Escolha uma das opções a seguir.\n[1] - Para somar\n[2] - Para subtraior\n[3] - Para multiplicação'
      f'\n[4] - Para divisão.')
res = int(input('R: '))

if res == 1:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    print(f'\nO resultado da soma dos seus números é {num1 + num2}')

elif res == 2:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    print(f'\nO resultado da subtração dos seus números é {num1 - num2}')

elif res == 3:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    print(f'\nO resultado da multiplicação dos seus números é {num1 * num2}')

elif res == 4:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    print(f'\nO resultado da divisão dos seus números é {num1 / num2}')
else:
    print(f'Não entendi o que você quis dizer.')

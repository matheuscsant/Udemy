print(f'Escolha uma das 4 opção a seguir.\n[1] Somar 2 números.\n[2] Diferença entre 2 números (maior pelo menor)'
      f'\n[3] Produto entre 2 números.\n[4] Divisão entre 2 números (Denominador não pode ser zero) ')
res = int(input('R: '))

if res == 1:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    print(f'A soma dos seus números é {num1 + num2}')
elif res == 2:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    if num1 > num2:
        print(f'A diferença entre seus números é de {num1 - num2}')
    else:
        print(f'A diferença entre seus números é de {num2 - num1}')
elif res == 3:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    print(f'\nO seu produto será {num1 * num2}')
elif res == 4:
    print(f'\nDigite um número')
    num1 = float(input('R: '))

    print(f'\nDigite outro número')
    num2 = float(input('R: '))

    if num2 == 0:
        print(f'\nDivisão inválida, denominador igual á 0')
    else:
        print(f'\nO resultado da sua divisão é {num1 / num2}')
else:
    print(f'\nOpção inválida, tente novamente.')

print(f'\nDigite um número')
num = int(input('R: '))

div5 = num % 5

div3 = num % 3

if div5 > 0:
    print(f'\nSeu número não é divisível por 5.\n')
else:
    print(f'\nSeu número é divisível por 5, e sua divisão dá {div5}\n')

if div3 > 0:
    print(f'\nSeu número não é divisível por 3.\n')
else:
    print(f'\nSeu número é divisível por 3, e sua divisão dá {div3}\n')

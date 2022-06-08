print(f'Digite um ano')
ano = int(input(f'R: '))

bissexto_400 = ano % 400
bissexto_4 = ano % 4
naobissexto = ano % 100

if bissexto_400 == 0 or bissexto_4 == 0 and naobissexto > 0:
    print(f'Seu ano é bissexto')

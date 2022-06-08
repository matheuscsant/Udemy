print(f'Digite em qual ano está')
ano = int(input(f'R: '))

print(f'Agora digite o mês')
mes = int(input(f'R: '))

print(f'E por último, o dia.')
dia = int(input(f'R: '))

anobissexto = ano % 4

if anobissexto > 0:
    if dia > 28 and mes == 2:
        print(f'Data inválida, somenta nos anos bissextos fevereiro tem 29 dias')

elif anobissexto == 0:
    if dia > 29 and mes == 2:
        print(f'Data inválida')

elif mes > 12:
    print(f'Data inválida')

elif dia > 30:
    print(f'Data inválida')

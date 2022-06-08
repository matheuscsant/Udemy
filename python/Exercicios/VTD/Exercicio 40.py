dias = int(input(f'\nQuantos dias o encanador trabalho trabalhou?\n'))

bruto = dias * 30.0
desconto = bruto * 0.08
liquido = bruto - desconto

print(f'\nO encanador trabalhou por {dias} dias, e receberá 30,00 R$ por dia, '
    f'levando em consideração\n que será descontado 8% para o imposto de renda, '
    f'o encanador ira receber {liquido} R$.\n')

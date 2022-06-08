print(f'Digite a quantia de venda mensal')
venda = float(input(f'R: '))

if venda >= 100000.0:
    comissao = 700 + (venda * 0.16)
    print(f'Sua comissão será de {comissao:.2f}')
elif 100000 > venda >= 80000:
    comissao = 650 + (venda * 0.14)
    print(f'Sua comissão será de {comissao:.2f}')
elif 80000 > venda >= 60000:
    comissao = 600 + (venda * 0.14)
    print(f'Sua comissão será de {comissao:.2f}')
elif 60000 > venda >= 40000:
    comissao = 550 + (venda * 0.14)
    print(f'Sua comissão será de {comissao:.2f}')
elif 40000 > venda >= 20000:
    comissao = 500 + (venda * 0.14)
    print(f'Sua comissão será de {comissao:.2f}')
elif 20000 > venda >= 0:
    comissao = 400 + (venda * 0.14)
    print(f'Sua comissão será de {comissao:.2f}')
else:
    print(f'O valor digitado é inválido')

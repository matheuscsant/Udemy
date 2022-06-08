print(f'\nOlá, qual seu valor de compras (A partir de R$ 100,00 você terá descontos)')
Preco = float(input('\nR: '))

Desconto = Preco * 0.1
ParcelasSJ = Preco / 3
ComissaoVista = Desconto * 0.05
ComissaoParcela = Preco * 0.05

print(f'\nSeu desconto será de {Desconto:.2f} Reais pagando então {Preco - Desconto} Reais, caso opte pelas parcelas em 3x sem juros\n '
    f'sairá {ParcelasSJ:.2f} Reais por mês, a comissão do vendedor á vista é {ComissaoVista:.2f} Reais e em parcelas\n '
    f'é de {ComissaoParcela:.2f} Reais\n')
    
print(f'Escolha uma das seguintes opções:\n'
      f'Código 100 - Cachorro quente - R$1,20\n'
      f'Código 101 - Bauru simples - R$1,30\n'
      f'Código 102 - Bauro com ovo - R$1,50\n'
      f'Código 103 - Hamburguer - R$1,20\n'
      f'Código 104 - CheeseBurguer - R$1,70\n'
      f'Código 105 - Suco - R$2,20\n'
      f'Código 106 - Refrigerante - R$1,00')
resposta = int(input(f'R: '))

print(f'\nQual a quantidade desejada do item?')
quant = int(input(f'R: '))

if resposta == 100:
    print(f'Você terá que pagar R${1.20 * quant}')
elif resposta == 101:
    print(f'Você terá que pagar R${1.30 * quant}')
elif resposta == 102:
    print(f'Você terá que pagar R${1.50 * quant}')
elif resposta == 103:
    print(f'Você terá que pagar R${1.20 * quant}')
elif resposta == 104:
    print(f'Você terá que pagar R${1.70 * quant}')
elif resposta == 105:
    print(f'Você terá que pagar R${2.20 * quant}')
elif resposta == 106:
    print(f'Você terá que pagar R${1.00 * quant}')
else:
    print(f'Código inválido, tente novamente.')

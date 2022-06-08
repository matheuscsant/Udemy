
print(f'Qual o valor de fábrica do carro que deseja comprar?')
res = float(input(f'R: '))

if res <= 12000:
     comissao_vendedor = (res * 0.05)
     imposto = 0 #no caso de 12.000 é isento o imposto
     custo_consumidor = res + comissao_vendedor + imposto
     print(f'O valor do seu carro será de R$ {custo_consumidor:.2f}')

elif 12000 < res < 25000 :
     comissao_vendedor = res * 0.10
     imposto = res * 0.15
     custo_consumidor = res + comissao_vendedor + imposto
     print(f'O valor do seu carro será de R$ {custo_consumidor:.2f}')
     
elif res >= 25000:
     comissao_vendedor = res * 0.15
     imposto = res * 0.20
     custo_consumidor = res + comissao_vendedor + imposto
     print(f'O valor do seu carro será de R$ {custo_consumidor:.2f}')

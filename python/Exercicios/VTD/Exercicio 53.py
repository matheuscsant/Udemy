print(f'\nQual o comprimento do terreno?')
comprimento = float(input('\nR: '))

print(f'\nQual a largura do terreno?')
largura = float(input('\nR: '))

print(f'\nE qual o preço por m² da tela?')
preco_tela = float(input('\nR: '))

area = comprimento * largura
preco_total = area * preco_tela

print(f'\nA área que precisa ser coberta é {area:.2f} M², logo o preço sendo {preco_tela:.2f} R$, teremos '
    f'que pagar {preco_total:.2f} R$ para cubrir toda a área\n')
    
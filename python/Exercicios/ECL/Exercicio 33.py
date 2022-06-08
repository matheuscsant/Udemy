print(f'Qual era o preço antigo?')
preco = float(input(f'R: '))
new_preco = 0

if preco >= 50.0:
    new_preco = preco + (preco * 0.05)
elif 50.0 < preco < 100.0:
    new_preco = preco + (preco * 0.1)
elif preco >= 100.0:
    new_preco = preco + (preco * 0.15)

if new_preco <= 80.0:
    print(f'O preço está barato.')

elif 80.0 < new_preco <= 120.0:
    print(f'O preço está normal.')

elif 120.0 < new_preco <= 200.0:
    print(f'O preço está caro.')

else:
    print(f'O preço está muito caro')

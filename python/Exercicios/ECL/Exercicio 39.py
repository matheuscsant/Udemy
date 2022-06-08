import sys

print(f'Qual o valor do seu salário bruto?')
valorSalario = float(input(f'R: '))

print(f'Quantos anos você tem de contribuição na empresa?')
anosContribuicao = int(input(f'R: '))

if 0 < valorSalario <= 500:
    newSalario = valorSalario * 1.25
elif valorSalario <= 1000:
    newSalario = valorSalario * 1.20
elif valorSalario <= 1500:
    newSalario = valorSalario * 1.15
elif valorSalario <= 2000:
    newSalario = valorSalario * 1.10
elif valorSalario > 2000:
    newSalario = valorSalario
else:
    print(f'\nSalário inválido')

if anosContribuicao < 1:
    print(f'\nTempo de contribuição não atingido para aquisição do bônus')
elif 1 <= anosContribuicao <= 3:
    newSalario = newSalario + 100
elif 4 <= anosContribuicao <= 6:
    newSalario = newSalario + 200
elif 7 <= anosContribuicao <= 10:
    newSalario = newSalario + 300
elif anosContribuicao > 10:
    newSalario = newSalario + 500

print(f'\nSeu novo salário será de R${newSalario:.2f}')
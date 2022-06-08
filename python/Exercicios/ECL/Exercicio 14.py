
print(f'\nQual foi sua nota de laboratório?')
notalab = float(input('R: '))

print(f'\nQual foi sua nota de Avaliação Semestral?')
notaava = float(input('R: '))

print(f'\nQual foi sua nota de Exame Final?')
notaexame = float(input('R: '))

result = ((notalab * 2) + (notaava * 3) + (notaexame * 5)) / 10


if result >= 5:
    print(f'Sua nota foi de {result} pontos, e você está aprovado, parabéns!')
elif 3 <= result <= 4.9:
    print(f'Sua nota foi de {result} pontos, e você está de recuperação.')
elif 0 <= result <= 2.9:
    print(f'Sua nota foi de {result} pontos, e você foi reprovado.')

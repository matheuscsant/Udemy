import random
acertos = 0
for questao in range(1, 6):
    num1 = random.randrange(1, 100)
    num2 = random.randrange(1, 100)
    result = num1 + num2
    print(f'\n[{questao}] - Qual a soma entre os números {num1} + {num2}?')
    res = int(input(f'R: '))
    if res == result:
        acertos = acertos + 1
        print(f'\nVocê acertou, parabéns =)')
    else:
        print(f'\nVocê errou, a resposta era {result}')
print(f'Seu total de acertos foi de {acertos}.')

salariobase = float(input('\nQual seu salário base?\n'))

ImpostRenda = salariobase * 0.07
gratificacao = salariobase * 0.05

newsalario = (salariobase + gratificacao) - ImpostRenda

print(f'Seu salário base é {salariobase} Reais, voce terá 5% de gratificação, que será de {gratificacao} Reais, '
    f'terá 7% descontados para o Imposto de Renda\n que será de {ImpostRenda:.2f}, e seu salário liquido será de '
    f'{newsalario} Reais')
    
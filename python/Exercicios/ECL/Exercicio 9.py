print(f'\nDigite seu salário (sem vírgulas).')
salario = float(input(f'\nR: '))

print(f'\nQual o valor do empréstimo que você deseja?')
emprestimo = float(input(f'\nR: '))

condicao = salario * 0.2

if emprestimo > condicao:
    print(f'\nEmprestimo não concedido.\n')
else:
    print(f'\nEmprestimo concedido.\n')

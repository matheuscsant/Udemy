'''
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.

#Exemplo 1
for i in range(1, 11):
    if i == 6:
        break
    else:
        print(i)
print('Saida do loop')

#Exemplo 2
while True:
    print(f'Digite "sair" para sair do loop. ')
    res = str(input(f'R: '))
    if res == 'sair':
        break

'''
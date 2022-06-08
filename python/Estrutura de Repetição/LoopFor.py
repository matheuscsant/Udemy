'''
Loop For

[1] Loop é estruturas de repetição
    [1.2] For é uma dessas estruturas

C ou Java:

for(int i = 0; i < 10; i++){
    //execução do loop
}

Para python:

for item in interável:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplo de iteráveis:
    - String
        nome = 'Matheus Campanhola'
    - Lista
        lista = [1, 3, 5, 7, 9]
    - Range
        numeros = range(1, 10)

#[1] Exemplo de for

for letra in nome:
    print(letra)

#[2] Exemplo de for (iterando sobre uma lista)

for numero in lista:
    print(numero)

#[3] Exemplo de for (iterando sobre um range)

range(valor_inicial, valor_final)

Obs: O valor final não é inclusive.

1
2
3
4
5
6
7
8
9
10 -> Não


for numero in range(1, 10):
    print(numero)   

Enumerate 

((0, 'M'), (1, 'a'), (2, 't'), (3, 'h'), (4, 'e'), ...) d


for indice, letra in enumerate(nome):
    print(nome[indice])


for indice, letra in enumerate(nome):
    print(letra)


for _, letra in enumerate(nome):
    print(letra)
Obs: Quando não precisamos de um valor podemos descarta-lo utilizando um underline(_)


nome = 'Matheus Campanhola'
lista = [1, 3, 5, 7, 9, 11]
numeros = range (1, 10)  #Temos que trasnformar em uma lista

for valor in enumerate(nome):
    print(valor[1])


qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0


for n in range(1, qtd + 1):
    numero = int(input(f'Informe o {n} / {qtd} valor: '))
    soma = soma + numero
print(f'A soma é {soma}.')


nome = 'Matheus Campanhola'
for letra in nome:
    print(letra, end='')

https://apps.timwhitlock.info/emoji/tables/unicode


'''

#Original: U+1F60D
#Modificado: U0001F60D
for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)

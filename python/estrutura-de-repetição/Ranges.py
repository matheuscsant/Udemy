'''
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências númericas, não de forma aleatória,
mas sim de maneira especeficada.

Formas gerais:

#Forma 1:
    range(valor da parada)

OBS:valor de parada não inclusivo (inicio padrão 0, e passa de 1 em 1)

    #Exemplo 1
for i in range(10):
    print(i)

#Forma 2:
    range(valor de inicio, valor de parada)

OBS:valor de parada não inclusivo (passa 1 em 1)

    #Exemplo 2
for i in range(1, 10):
    print(i)

#Forma 3:
    range(valor de inicio, valor de parada, passo)

OBS:valor de parada não inclusivo (passo especificado pelo usuario)

    #Exemplo 3
    for i in range(1, 10, 2):
    print(i)

#Forma 4 (Inversa da forma 3): 
    range(valor de inicio, valor de parada, passo)

OBS:valor de parada não inclusivo (valor inicio especificado pelo usuario e passo especificado pelo usuario)

    Exemplo 4:
    for i in range(10, 0, -1):
    print(i)

'''
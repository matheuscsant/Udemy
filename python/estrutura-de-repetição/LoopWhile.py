'''
Loop While

Forma geral:

while expresão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a exprre~soa booleana for verdadeira.

Expressão booleana é toda expresão onde o resultado é verdadeiro ou falso.

Exemplo:
num = 5

num < 5

#Exemplo 1:
    numero = 1

    while numero < 10:
        print(numero)
        numero = numero + 1

    #OBS: em um loop while, é importante que cuidemos do critério de parada, para não causar um loop infinito.

#Exemplo 2:
    res = ''

    while res != 'sim':
        print(f'Ja terminou o programa?')
        res = str(input(f'R: '))

Em Java/C 
while(expressão){
    //execução
};

do{
    //execução
}while(expressão);
'''

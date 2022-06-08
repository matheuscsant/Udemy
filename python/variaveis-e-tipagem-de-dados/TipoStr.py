"""
String

[1]Em python, um dado é considerado do tipo string sempre que:

 - Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3';
 - Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3";
 - Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3''';

Exemplos

nome = 'Matheus'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie' -> \n é o enter, serve para pular de linha.
print(nome)
print(type(nome))

nome = 'Matheus Campanhola'

print(nome.lower()) -> Tudo minúsculo
print(nome.upper()) -> Tudo maiúsculo

print(nome.split()) -> Transforma em uma lista de strings
['Matheus', 'Campanhola']

[2] Como o python armazena strings:

nome = 'Matheus Campanhola'
['M', 'a', 't', 'h', 'e', 'u', 's', ' ', 'C', 'a', 'm', 'p', 'a', 'n', 'h', 'o', 'l', 'a']
[ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10,  11,  12,  13,  14,  15,  16,  17]

print(nome[0:7]) -> Ira imprimir Matheus (Slice de String)
print(nome[8:18]) -> Ira imprimir Campanhola (Slice de String)

print(nome.split()[0]) -> Ira imprimir Matheus
print(nome.split()[1]) -> Ira imprimir Campanhola
['Matheus', 'Campanhola']

nome = 'Matheus Campanhola'
print(nome[::-1]) -> Metodo Pythônico para inversão da string
alohnapmaC suehtaM

nome = 'Matheus Campanhola'
print(nome)
print(nome.replace('M', 'G')) -> Substitui M por G

Palíndromos (O inverso é o mesmo):

texto = 'socorram me subino onibus em marrocos'
print(texto)
print(texto[::-1])

nome = 'ana'
print(nome)
print(nome[::-1])

"""


# - Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3""";
# 
# nome = """Angelia 
# Jolie"""
# print(nome)
# print(type(nome))
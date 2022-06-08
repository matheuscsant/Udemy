'''
Escopo de Variáveis (Espaço de variáveis)

Dois casos de escopo:

[1] Variáveis globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

[2] Variáveis locais;
    - Variáveiis locais são reconhecidas, apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada

Para declarar variáveis em Python, fazemos:

nomeVar = ValordaVariavel
numero = 42
nome = Matheus
bool = True

Python é uma linguagem de tipagem dinâmica, isso significa que ao declararmos uma variável, nós não colocamos
o tipo de dado dela; este tipo é inferido ao atribuírmos à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;

Exemplo de Variavel Global (Pode ser declarada em qualquer lugar do código):
numero = 42
print(numero)
print(type(numero))

numero = 'Geek' -> Reatribuição (Python tipa de dado, conforme o valor que estiver na var)
print(numero)
print(type(numero))

Exemplo de Variavel Local (Precisa ser declarada dentro do seu bloco onde for usada):
numero = 2
if numero > 10:
    novo = numero + 10
    print(novo)

'''

'''
 Estruturas Lógicas

 Operadores unários:
    - not;
 Operadores binários:
    - and, or, is

 [1] And, para and, ambos os valores precisam ser True para execução do bloco
    
    Ativo = True
    Logado = True

    if Ativo and Logado:
        print('Bem - Vindo usuário.')
    else:
        print('Você precisa ativar sua conta, por favor check seu email.')

 [2] Or, para or, um ou outro valor precisa ser true, se ambos forem False, não executa o bloco
    
    [2.1] Exemplo que executará o código:
    
        Ativo = True
        Logado = False

        if Ativo or Logado:
            print('Bem - Vindo usuário.')
        else:
            print('Você precisa ativar sua conta, por favor check seu email.')
    
    [2.2] Exemplo que não executará o código
        
        Ativo = False
        Logado = False

        if Ativo or Logado:
            print('Bem - Vindo usuário.')
        else:
            print('Você precisa ativar sua conta, por favor check seu email.')

 [3] Not, para not, o valor do booleano é invertido, ou seja, True vira False, e False vira True.
    
    Ativo = True
    Logado = False

    if not Ativo:
        print('Você precisa ativar sua conta, por favor, cheque seu e-mail.')
    else:
        print('Bem - Vindo usuário')


 [4] Is, para o is, o valor é comparado com um segundo valor.

    Ativo = True
    Logado = False

    if Ativo is True:
        print('Bem - Vindo usuário')
    else:
    print('Você precisa ativar sua conta, por favor, cheque seu e-mail.')

'''

Ativo = True
Logado = False

if Ativo is True:
    print('Bem - Vindo usuário')
else:
   print('Você precisa ativar sua conta, por favor, cheque seu e-mail.')
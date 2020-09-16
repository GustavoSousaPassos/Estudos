"""

        CURSO EM VIDEO PYTHON MUNDO 3 : ESTRUTURAS COMPOSTAS

            - () : Tuplas
            - [] : Listas
            - {} : Dicionarios

        AULA 72: Tuplas

            - São variaveis compostas que armazenam multiplos valores (ex : string)
            - São IMUTAVEIS, ou seja, nãop se pode atr4ibuir outros valores
            - Como fazer:

                var = (val1 , val2, etc) - Criando uma tupla
                var(x) - Mostra o valor alocado na posição x
                var(0:x) - Mostra os valores da primeria pos. até anterioir de x(x no caso vai nser ignorado)
                var(x:) - Da posição x até a ultima da tupla

            - len() - Mostra a quantidade de valores alocados na tupla
            - index(val, pos_inicial) - Mostra a possição que se encontra o val
            - del(n_tupla) - Apaga a tupla
            - sorted() - Organiza a tupla em ordem alfabetica(esse comando faz com a variavel torne-se uma lista)
            - Pode-se usar os mesms comandos usados para manipuação de string

lanche = ('a', 'b', 'c')

        for c in range(0,len(lanche):  OU for in lanche:
            print(f'{c}') # Imprimi apenas os valores sem os elementos da tupla

del(lanche)
print(lanche.index('b'))
"""

num = ('zero', 'um', 'dois', 'três', 'quarto', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'deseseis', 'desesete', 'desoito', 'desenove','vinte')
while True:
    val = int(input('Digite um número entre 0 e 20: '))
    if val <= len(num) and val >= 0:
        print(f'Você digitou {num[val]}')
        break
    else:
        print('Digite um número apenas entre 0 e 20')

 #BIBLIOTECA MATH **
#
# ceil- arrendondamento para cima
# floor -- arredondar para baixo
# trunc -- Ele vai "Truncar", ou seja, eliminar da virgula até a direita sem arredondar
# pow -- Potencia
# sqrt (square root)-- faz raiz quadrada
# factorial -- Calcula o fatorial
#
# import math -- GENERALIZAÇÃO  <<:  var = math.pow(num)
# from math import sqrt, trunc -- ESPECIFICAÇÃO <<:  var = pow(num)
#help('modules') // mostra todas as bibliotecas instaladas  no terminal

from math import trunc
a = float(input('digite um número'))
print(trunc(a))

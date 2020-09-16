f = str(input('Digite ua frase qualquer: ')).strip().upper()
p = f.split()                                               # Criando uma lista de palavras
j = ''.join(p)                                              # Juntando novamente em uma string, mas eliminando os espaços
inverso = ''
for letra in range(len(j) -1, -1, -1 ):                     # Invertendo a frase
    inverso += j[letra]

if inverso == j:
    print('Polindromo')
else:
    print('Polindromo não encontrado')


#Segunda maneira (a que foi relizada):

'''f = str(input('Digite uma frase qualquer: '))
f.strip()
a = f[::-1]
if a == f:
    print('Polidromo')
else:
    print('Não é polidromo')'''


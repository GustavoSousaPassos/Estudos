# <-------      CADEIA DE CARACTERES = STRING    ------->

#                  FATIAMENTO  DE STRING = RANGE
#  #FATIAMENTO
#
#    - Frase[x]: refere-se ao caracter que se encontra na posição indicada
#    - Frase[x:y]: seleciona um conjunto a parti de uma posição inicial(x) até a posição anterior da final(y)
#    - Frase[x:y:z]: semelhante ao anterior, porém, ele efetua salto sequenciais (z) que selecionam apenas determinados
#                    caracteres que estão dentro do conjunto selecionado(x:y)
#           Ex: frase = 'caracolina' ; print(frase[1:5:2]) ; RESULTADO = 'aoia'
#
#    - Frase[:x] : Seleciona um conjunto a parti da posição inicial(0) até a anterior da final(x)
#    - Frase[x:] : Seleciona um conjunto da posição determinada(x) até a ultima existente
#
#  #COMANDOS
#
#   - len() - mostra o tamanho
#   - count() - mostra a quantidade de repetições do(s) caracter(es) na string
#   - find('caracter ou string que deseja') - encontra e mostra a posição do(s) caracter(es) selecionados
#   - reaplace('string existente','string que substituira') - substitue um string por outra
#           OBS: Caso a substituição seja maior, e adicionado mais espaços na string
#   - upper()/lower() - Altera a string em maiusculo/minusculo
#   - capitalize() - Apenas deixa a primeira posição da string em maiusculo
#   - title() - Analisa a quantidade de palavras contida na string, a parti dos espaços vazios. Para cada letra inicial
#               ele deixa em maiscula
#   - strip() - Elimina todos os espaços vazios iniciais e finais, sem afetar nos do centro
#           *rstrip/lstrip - elimina apenas na direita/esquerda
#   - split() - Metodo que analisa a string e, determinando a quantidade de palavras  diacorddo com os espaços vazios
#              entre as palavras, ele vai gerar nova(s) string(s), ou seja, de uma cadeia ele vai gerar um lista de
#              strings.
#   - 'char'.join() - substitui os espaços vazios pelo caracter determinado

a = str(input('Digite seu nome: ')).strip()
print('Nome em maisculo: {}{}{}'.format('\033[30;45m',a.upper(),'\033[m'))
print('Nome em minusculo: {}{}{}'.format('\033[46m',a.lower(),'\033[m'))
print('Tamanho do nome completo: {}{}{}'.format('\033[41m',len(a)-a.count(' '),'\033[m'))
d = a.split()
print('O tamanho do seu primeiro nome: {}{}{}'.format('\033[36m',len(d[0]),'\033[m'))
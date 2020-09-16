from datetime import date
ano = int(input('Digite um ano qualquer, caso queira o ano atual, digite 0: '))
#Conteúdo extra da aula:
if ano == 0:
    ano = date.today().year                     #coloca a data de hoje, no caso, apenas o ano é selecionado
    print('Estamos no ano de {}'.format(ano))
print('Esse ano é bissexto!' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else'Esse ano não é bissexto!')

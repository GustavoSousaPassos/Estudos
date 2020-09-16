tabela = ('Flamengo', 'Palmeiras', 'Santos', 'Internacional','Corihians','São Paulo','Bahia','Gremio','Atletico MG','Botafogo','Atletico PR','Vasco','Ceará','Fortaleza','Goias','Fluminense','Cruzeiro','CSA','Chapecoense','Avaí')
print(f'Primeiros colocados')
for pos,c in enumerate(tabela[:5]):
    print(f'    {pos} - {c}')

print('\n Ultimos colocados: ')
for pos, x in enumerate(tabela[16:20]):
    print(f'          - {x}')

tab_s = sorted(tabela)                      # coloca os valores e ordem alfabetica
print(f'\n Times em ordem alfabetica')
for y in tab_s[0:]:
    print(f'     {y}')

print(f"Posição da Chapecoense: {tabela.index('Chapecoense')+1}")
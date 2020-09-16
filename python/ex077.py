t = ('ana','velho', 'mexirica', 'folgado', 'louco', 'barba')
for pos, c in enumerate(t[0:]):
	p = c
	print (f'A palavra e {c} e suas vogais são : ')
	for pos, d in enumerate(p[0:]):
		if d == 'a' or d == 'e' or d == 'i' or d == 'o' or d == 'u':
			print(f'{d}', end="")
	print('\n')

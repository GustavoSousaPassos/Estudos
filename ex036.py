val_c = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
a = int(input('Digite agora o tempo que pretende pagar: '))
p = val_c / (a*12)
sal_p = sal * 0.3
if p < sal_p:
	print('Valor das parcelas: R${:.2f}'.format(p))
elif p >= sal_p:
	print('Você não podera finaciar essa casa!')
else:
	print('Valor das parcelas: R${:.2f}'.format(p))

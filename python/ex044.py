pr = float(input('Digite o preço da comprar'))
opc = int(input('Digite a opção de pagamento desejado: \n[1] A vista \n[2]A vista no cartão \n[3] Até 2x no cartão \n[4] 3x  ou maisno cartão'))
if opc == 1:
    d = pr * 0.1
    pr = pr - d
    print('Total a pagar: {:.2f}'.format(pr))
elif opc == 2:
    d = pr * 0.5
    pr = pr - d
    print('Total a pagar: {:.2f}'.format(pr))
elif opc == 3:
    p1 = pr / 2
    print('Total da parcela a pagar: {:.2f}'.format(p1))
elif opc == 4:
    qtd_p = int(input('Quantas parcelas? '))
    p1 = pr / qtd_p
    j = p1 * 0.2
    pr_j = p1 + j
    print('Total da parcela: {:.2f} \nTotal a pagar: {:.2f}'.format(pr_j, pr + pr_j))

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
count = 0
while count == 0:
    opc = int(input('Qual opção você deseja? \n [1] Soma \n [2] Multiplicar \n [3] Maior \n [4] Digitar novos números \n [5] Sair \n opção: '))
    if opc == 1:
        s = num1 + num2
        print('A soma total dos núeros digitados fica: {}'.format(s))
    elif opc == 2:
        m = num1 * num2
        print('O resultado será: {}'.format(m))
    elif opc == 3:
        if num1 > num2:
            print('O núero maior digitado foi o primeiro!')
        else:
            print('O número maior digitado foi o segundo!')
    elif opc == 4:
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    elif opc == 5:
        count = 1
    else:
        print('Opção ínvalida! Tente novamente!')

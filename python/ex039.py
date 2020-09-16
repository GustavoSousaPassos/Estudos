#Para alistamento, informa o tempo que falta ou  o quue já passou
id = int(input('Digite sua idade'))
if id < 18:
    t1 = 18 - id
    print('Você ainda é muito jovem para se alistar, volte daqui uns {} anos'.format(t1))
elif id == 18:
    print('Está na hora de você se alistar!')
else:
    t2 = id - 18
    print('Você já passou do tempo de se alistar! \ntempo ultrapassado: {}'.format(t2))

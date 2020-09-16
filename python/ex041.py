id = int(input('Digite sua idade jogador: '))
if id <= 9:
    print('Você entrará no grupo mirim')
elif id <= 14:
    print('Você vai ficar no time infantil')
elif id <= 19:
    print('Você está no time junior agora!')
elif id == 20:
    print('Time sênior')
else:
    print('Time master!')
    
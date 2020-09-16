import pygame
#inicialização da função mixer
pygame.mixer.init()
#comando para selecionar o arquivo a ser processado
pygame.mixer.music.load('music_3.mp3')
#comando para executar o arquivo
pygame.mixer.music.play()
input()
#PAra deixar o evento na fila, ou seja esperando, a musica ficara no modo ocioso, e o evento acabará depois deser retornado
pygame.event.wait()
# ESSE EU NÃO CONSEGUI FAZER SOZINHO
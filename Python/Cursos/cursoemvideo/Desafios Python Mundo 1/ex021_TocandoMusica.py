#Crie um programa que abra um arquivo.mp3 e toque a música sozinho.

import pygame

musica = 'Tobu_Colors.mp3'

#Inicializa o mixer do pygame
pygame.mixer.init()

#Carrega o arquivo MP3
pygame.mixer.music.load(musica)

#Toca o arquivo MP3
pygame.mixer.music.play()

#Mantem o script rodando enquanto a música toca
while pygame.mixer.music.get_busy():
    pass

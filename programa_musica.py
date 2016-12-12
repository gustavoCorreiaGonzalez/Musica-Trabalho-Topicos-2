import time, sys, os
import numpy as np
import pygame

instrumentos = {0:"cavaco", 1:"violao", 2:"chocalho"}

votos = {}

votos = np.zeros(8)

botao = ''

votacao_concluida = 0

cavaco = None
violao = None
chocalho = None

pygame.init()
pygame.mixer.init()
violao = pygame.mixer.Sound(instrumentos[1]+".ogg")
cavaco = pygame.mixer.Sound(instrumentos[0]+".ogg")
chocalho = pygame.mixer.Sound(instrumentos[2]+".ogg")
violao.play()
cavaco.play()
chocalho.play()
violao.set_volume(1)
cavaco.set_volume(0)
chocalho.set_volume(0)

def espera():
	print('Votacao encerrada')
	time.sleep(5)
	print('Proxima votacao')

def votacao():
	global votacao_concluida

	if votacao_concluida == 1:
		espera()
		votacao_concluida = 0

	votos = {}

	votos = np.zeros(8)

	botao = ''

	i = 0
	while(i < 2):
		print('Digite o numero do instrumento:')
		print('1. Cavaco')
		print('2. Chocalho')
		botao = input()

		os.system('cls' if os.name == 'nt' else 'clear')

		if (int(botao) >= 1 and int(botao) <= 2):
			votos[botao]+=1 
			i+=1

	votacao_concluida = 1

	return votos

def toca_instrumentos(tocando, instrumento=''):
	if instrumento == 1:
		cavaco.set_volume(1)

	if instrumento == 2:
		chocalho.set_volume(1)

	if tocando == 1:
		while True:
			votos = votacao()

			toca_instrumentos(2, np.argmax(votos))

if __name__ == "__main__":
    toca_instrumentos(1)
import time, sys, os
import numpy as np
#import pygame

instrumentos = {0:"cartoon001", 1:"cartoon012"}

def toca_instrumento(instrumento):
	# pygame.init()
	# pygame.mixer.init()
	# sound = pygame.mixer.Sound(instrumentos[instrumentos]+".wav")
	# sound.play()
	print(instrumentos[instrumentos])

votos = {}

votos = np.zeros(8)

botao = ''

i = 0
while(i < 8):
	print('Digite o numero do instrumento')
	print('0. Violao parte 1')
	print('1. Cavaco parte 1')
	print('2. Mari cantando')
	print('3. Piano')
	print('4. Reco-Reco')
	print('5. Chocalho')
	print('6. Violao parte 2')
	print('7. Cavaco parte 2')
	botao = input()

	os.system('cls' if os.name == 'nt' else 'clear')

	if (int(botao) >= 1 and int(botao) <= 8):
		votos[botao]+=1 
		i+=1

toca_instrumento(np.argmax(votos))

# while key != ord('q'):
# 	key = stdscr.getch()
# 	stdscr.refresh()

# 	if key == curses.KEY_LEFT:
# 		pygame.init()
# 		pygame.mixer.init()
# 		sound = pygame.mixer.Sound("cartoon0121.wav")
# 		sound.play()
# 	if key == curses.KEY_DOWN: 	
# 		pygame.init()
# 		pygame.mixer.init()
# 		sound = pygame.mixer.Sound("cartoon0121.wav")
# 		sound.play()

# 	time.sleep(5)






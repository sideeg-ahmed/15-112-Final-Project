import pygame
import random
import leo
import ken


pygame.init()
#comments and more important comments
mainMenu = pygame.display.set_mode((965 , 715))
bg = pygame.image.load('main menu.png')
#comments and more important comments and more important comments
cursor = pygame.transform.scale2x(pygame.image.load('cursor.png'))
pygame.display.set_caption('Sidreet Fighter')
clock = pygame.time.Clock()
cursorY = 350
#thank god for comments
instructions = pygame.image.load('instruction.png')
instruc = False
def redrawMainMenu():
	#deserve full style points
	if not instruc: 
		mainMenu.blit(bg,(0,0))
		mainMenu.blit(cursor,(15,cursorY))
	else:
		mainMenu.blit(instructions,(0,0))
	pygame.display.update()

over = False
#comments and more important comments

while not over:
	#comments and more important comments
	clock.tick(13)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			over = True
	
	keys = pygame.key.get_pressed()	
	#decription of important stuff
	if keys[pygame.K_DOWN] and cursorY < 350 +120*2:
		cursorY += 120
	#comments everywhere
	elif keys[pygame.K_UP] and cursorY > 350:
		cursorY -= 120
	if keys[pygame.K_SPACE]:
		print 'sda'
		if cursorY == 350:
			over = True
			import twoPlayer
		#yup looks good
		if cursorY == 350+120:
			over = True
			import vsCom
			
		if cursorY == 350+120*2:
			instruc = True
	#more comments
	if keys[pygame.K_ESCAPE]:
		instruc = False
			
	if not over:
		redrawMainMenu()
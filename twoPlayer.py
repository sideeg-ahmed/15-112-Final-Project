
import pygame
import time
import leo
import ken
import time
pygame.init()

mainMenu = pygame.display.set_mode((965 , 715))
clock = pygame.time.Clock()
cursor = pygame.transform.scale2x(pygame.image.load('cursor.png'))
cursor2 = pygame.transform.flip(pygame.transform.scale2x(pygame.image.load('cursor.png')),True,False)
cursorY = 250
cursorX = 10
select = True
maps = pygame.image.load('maps.png')
back = pygame.image.load('back.png')
playerz = [pygame.transform.scale2x(pygame.image.load('ken.png')),pygame.transform.scale2x(pygame.image.load('leona.png'))]
charselec = pygame.image.load('characterSelect.png')
bckg  = []
for i in range(1,5):
	bckg.append(pygame.transform.scale2x(pygame.image.load('Bckgrnd'+str(i)+'.png')))
n  = 0
winner = [pygame.transform.scale2x(pygame.image.load('output-onlinepngtools (1).png')),pygame.transform.scale2x(pygame.image.load('output-onlinepngtools (2).png'))]
char = False
def redrawMainMenu():
	if not char:
		mainMenu.blit(back,(0,0))
		mainMenu.blit(bckg[n],(0,160))
		mainMenu.blit(maps,(0,0))
		mainMenu.blit(cursor,(cursorX,cursorY))


		
	else:
		mainMenu.blit(charselec,(0,0))
		mainMenu.blit(cursor,(cursorX,cursorY))
		mainMenu.blit(cursor2,(cursorX2,cursorY2))
		mainMenu.blit(playerz[c-1],(653,112))
		mainMenu.blit(playerz[c2-1],(130,112))
	pygame.display.update()




while select:
	clock.tick(13)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			select = False
	
	keys = pygame.key.get_pressed()	
	if keys[pygame.K_DOWN] and cursorY < 250 +320:
		cursorY += 320
		if cursorX > 10:
			n  = 3-1
		else:
			n = 2-1
	elif keys[pygame.K_UP] and cursorY > 250:
		cursorY -= 320
		if cursorX > 10:
			n  = 4-1
		else:
			n = 1-1
	elif keys[pygame.K_RIGHT] and cursorX < 480:
		cursorX += 480-10
		if cursorY < 250+320:
			n  = 4-1
		else:
			n = 3-1
	elif keys[pygame.K_LEFT] and cursorX > 10:
		cursorX -= 480-10
		if cursorY  < 250+320:
			n  = 1-1
		else:
			n = 2-1

	if keys[pygame.K_SPACE]:
		
		select = False
	if select:
		redrawMainMenu()


char = True
select = True
cursorY = 540
cursorX = 227
cursorY2 = 540
cursorX2= 227
c = 1
c2 = 1
stop = False
stop2 = False
while select:
	clock.tick(13)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			select = False
	
	keys = pygame.key.get_pressed()	
	
	if keys[pygame.K_RIGHT] and cursorX < 515 and not stop:
		cursorX = 515
		c=2
	elif keys[pygame.K_LEFT] and cursorX > 227 and not stop:
		cursorX = 227
		c=1
	elif keys[pygame.K_d] and cursorX2 < 515 and not stop2:
		cursorX2 = 515
		c2=2
	elif keys[pygame.K_a] and cursorX2 > 227 and not stop2:
		cursorX2 = 227
		c2=1

	if keys[pygame.K_RSHIFT]:
		stop = not stop
	if keys[pygame.K_SPACE]:
		stop2 = not stop2
	if stop and stop2:
		select = False
	if select:
		redrawMainMenu()


screen = pygame.display.set_mode((640, 218))
pygame.display.set_caption('Sidreet Fighter')

if c == 1:
	player1 = ken.character(400,screen,1,-80)
else:
	player1 = leo.leona(400,screen,1,-80,)

if c2 == 1:
	player2 = ken.character(100,screen,2,80)
else:
	player2 = leo.leona(100,screen,2,80,)









bg = pygame.image.load('Bckgrnd'+str(n+1)+'.png')
done = False
explosion = []
for j in range(1,4):
	for i in range(4):
		explosion.append(pygame.transform.scale2x(pygame.image.load('image_1_'+str(j)+'(1).png')))

booom = False
healthBar = [pygame.image.load('BackHealth.png'),pygame.image.load('FrontHealth.png')]
energyBars = [pygame.image.load('energyback.png'),pygame.image.load('energyfront.png')]


def redrawGameWindow():
	global booom
	screen.blit(bg,(0,0))
	if player2.health < 0:
		player2.health = 0
	pygame.draw.rect(screen,(0,255,0),(165,20,player2.health,9))
	pygame.draw.rect(screen,(0,255,0),(330,20,player1.health,9))
	screen.blit(healthBar[0],(160,10))
	screen.blit(healthBar[1],(160,10))
	pygame.draw.rect(screen,(0,100,255),(32,205,player2.energy,9))
	pygame.draw.rect(screen,(0,100,255),(640-28-106,205,player1.energy,9))
	screen.blit(energyBars[0],(30,200))
	screen.blit(energyBars[1],(30,200))
	screen.blit(energyBars[0],(640-30-106,200))
	screen.blit(energyBars[1],(640-30-106,200))
	player1.redrawCharacter()
	player2.redrawCharacter()
	
	if booom:
		
		for i in range(12):
			screen.blit(explosion[i],(int(player2.hit[0]) , 140))
		booom = False		
	
	'''pygame.draw.rect(screen,(0,0,255),player1.hit,2)
				pygame.draw.rect(screen,(255,0,0),player1.body,2)
		
				pygame.draw.rect(screen,(255,0,0),player2.body,2)'''
	#pygame.draw.rect(screen,(0,0,255),player2.hit,2)

	
	
	
	pygame.display.update()

def checkCollision():
	global booom
	#player 1 hitting
	if int(player1.hit[0]) in range(int(player2.hitbox[0])-15, int(player2.hitbox[0]) + int(player2.hitbox[2])) and int(player1.hit[1]) in range(int(player2.hitbox[1])-10, int(player2.hitbox[1]) + int(player2.hitbox[3])):
		#player1.lock = True
		
		player2.lock = True

		if player1.hadouken or player2.isJump:
			
			player2.blck =False
			player2.lock = True
			player2.drop = True
			if player1.hadouken:
				player1.boom = True
				player2.health -= 20
			else:
				player2.health -= 0.7
			
		               
		elif player1.heavy :
			player2.blck =False
			player2.striked = True
			player2.rektCount = 2
			player2.health -= 0.7
		elif player1.punch and not player2.blck:
			player2.striked = True
			player2.health -= 0.5
			player2.rektCount += player1.punchCount/3
		elif player1.airPunch and not player2.blck:
			player2.striked = True
			player2.rektCount = 1
			player2.health -= 0.5
		player2.startRTimer = True

	#player 2 hitting
	if int(player2.hit[0]) + player2.hit[2]  in range(int(player1.hitbox[0]), int(player1.hitbox[0]) + int(player1.hitbox[2])+15) and int(player2.hit[1]) in range(int(player1.hitbox[1])-10, int(player1.hitbox[1]) + int(player1.hitbox[3])):
		
		player1.lock = True
		

		if player2.hadouken or player1.isJump:
			
			player1.blck =False
			player1.lock = True
			player1.drop = True
			if player2.hadouken:
				player2.boom = True
				player1.health -= 20
			else:
				player1.health -= 0.7
		               
		elif player2.heavy :
			player1.blck =False
			player1.striked = True
			player1.rektCount = 2
			player1.health -= 0.7

		elif player2.punch and not player1.blck:
			player1.striked = True
			player1.rektCount += player2.punchCount/3
			player1.health -= 0.5
		elif player1.airPunch and not player1.blck:
			player1.striked = True
			player1.rektCount = 1
			player1.health -= 0.5
		player1.startRTimer = True
	


	if player1.hadouken and player2.hadouken and (int(player2.hit[0])  < int(player1.hit[0])):
		if (int(player2.hit[0] +player2.hit[2]+25)   > int(player1.hit[0])):
			player1.boom =True
			player2.boom =True
			booom = True
		
		


while not done:

	clock.tick(13)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done = True
		
	keys = pygame.key.get_pressed()	
	
	if keys[pygame.K_RSHIFT] and not player1.isJump:
		player1.isJump = True

	if keys[pygame.K_SPACE] and not player2.isJump:
		player2.isJump = True

	   ###################################



	checkCollision()


	   ##################################
	 #light attack x
	if keys[pygame.K_x] and not player2.lock:
		
		#air counter is for making only a maximum of one combo in mid air               
		if player2.isJump and player2.airCounter < 3:
			player2.airCounter +=1
			player2.lock = True
			player2.airPunch = True
			player2.startPunchTimer = True
			if player2.punchTimer > 5:
				
				player2.punchTimer = False
				player2.airPunchCount = 0           
				
		
		elif not player2.isJump:

			player2.lock = True
			player2.punch = True

			player2.startPunchTimer = True
			if player2.punchTimer > 5:
				
				player2.punchTimer = False
				player2.punchCount = 0

	#light attack j
	if keys[pygame.K_j] and not player1.lock:
		
		#air counter is for making only a maximum of one combo in mid air				
		if player1.isJump and player1.airCounter < 3:
			player1.airCounter +=1
			player1.lock = True
			player1.airPunch = True
			player1.startPunchTimer = True
			if player1.punchTimer > 5:
				
				player1.punchTimer = False
				player1.airPunchCount = 0			
				
		
		elif not player1.isJump:

			player1.lock = True
			player1.punch = True

			player1.startPunchTimer = True
			if player1.punchTimer > 5:
				
				player1.punchTimer = False
				player1.punchCount = 0

	###########################################################
	#heavy attack k
	if keys[pygame.K_k] and not player1.lock:
		player1.lock = True
		player1.heavy = True

	#heavy attack c
	if keys[pygame.K_c] and not player2.lock:
		player2.lock = True
		player2.heavy = True
		
	   ##############################################

	#hadouken v
	if keys[pygame.K_v] and not player2.lock and player2.energy >= 25:
		player2.energy -= 25
		player2.fireX = player2.x + 80
		player2.walkCount = 0
		player2.lock = True
		player2.hadouken = True


	#hadouken l
	if keys[pygame.K_l] and not player1.lock and player1.energy >= 25:
		player1.energy -= 25
		player1.fireX = player1.x + 80
		player1.walkCount = 0
		player1.lock = True
		player1.hadouken = True

	###########################################	
	#blocking
	if keys[pygame.K_SEMICOLON] and not player1.lock:
		player1.lock = True
		player1.blck = True

	if keys[pygame.K_b] and not player2.lock:
		player2.lock = True
		player2.blck = True	

	if not keys[pygame.K_b]:
		player2.blck = False
	if not keys[pygame.K_SEMICOLON]:
		player1.blck = False



	##############################################	

	#move Left 
	if keys[pygame.K_LEFT] and player1.x > player1.speed-player1.width/2 and not player1.lock and player1.x > int(player2.body[0]) - 25:
		if player1.isJump:
			player1.x -= player1.speed
		else:
			player1.startLTimer = True
			
			if 4 > player1.Ltimer >= 2 and player1.x > 20-player1.width/2 and not player1.lock and player1.x > int(player2.body[0]) + 30:
				player1.startLTimer = False
				player1.Ltimer = 0
				
				player1.bdash = True

			else:
			
				player1.Ltimer = 0
				player1.x -= player1.speed
				player1.left = True
				player1.right = False

	#move Left 
	if keys[pygame.K_a] and player2.x > player2.speed-player2.width/2 and not player2.lock:
		if player2.isJump:
			player2.x -= player2.speed
		else:
			player2.startLTimer = True
			
			if 4 > player2.Ltimer >= 2 and player2.x > 20-player2.width/2:
				player2.startLTimer = False
				player2.Ltimer = 0
				
				player2.bdash = True

			else:
			
				player2.Ltimer = 0
				player2.left = True
				player2.x -= player2.speed
				
				player2.right = False

			
	#move right
	if keys[pygame.K_d] and player2.x < 640 - player2.width - player2.speed and not player2.lock and player2.x + int(player2.body[2])+20 < int(player1.body[0])-65:

	
		if player2.isJump:
			player2.x += player2.speed
		else:
			player2.startTimer = True
			if 4 > player2.timer >= 2 and player2.x < 640- player2.width - player2.speed-20 and player2.x + int(player2.body[2])+20 < int(player1.body[0])-90:
				player2.startTimer = False
				player2.timer = 0
				
				player2.fdash = True
			else:
				player2.timer = 0
				player2.right = True
				player2.x += player2.speed

				
				player2.left = False


	#move right
	if keys[pygame.K_RIGHT] and player1.x < 640 - player1.width - player1.speed and not player1.lock:

	
		if player1.isJump:
			player1.x += player1.speed
		else:
			player1.startTimer = True
			if 4 > player1.timer >= 2 and player1.x < 640- player1.width - player1.speed-20:
				player1.startTimer = False
				player1.timer = 0
				
				player1.fdash = True
			else:
				player1.timer = 0
				player1.x += player1.speed

				player1.right = True
				player1.left = False

	if player1.energy < 100:
		player1.energy += 0.5
	if player2.energy < 100:
		player2.energy += 0.5
	


	if player1.startTimer:
		player1.timer += 1
	if player1.startPunchTimer:
		player1.punchTimer += 1
	if player1.startLTimer:
		player1.Ltimer += 1

	if player2.startTimer:
		player2.timer += 1
	if player2.startPunchTimer:
		player2.punchTimer += 1
	if player2.startLTimer:
		player2.Ltimer += 1
	if player1.startRTimer:
		player1.rektTimer += 1
	if player2.startRTimer:
		player2.rektTimer += 1

		
	
	redrawGameWindow()


pygame.quit()

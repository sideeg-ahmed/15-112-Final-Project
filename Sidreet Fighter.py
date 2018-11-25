import pygame
import time
pygame.init()
screen = pygame.display.set_mode((640, 218))
pygame.display.set_caption('Sidreet Fighter')
clock = pygame.time.Clock()
bg = pygame.image.load('Bckgrnd3.png')
done = False
class character:
	def __init__(self):
		self.speed = 7
		self.height = 100
		self.width = 80
		self.x,self.y = 100,100
		self.walkCount = 0
		self.standCount = 0
		self.dashCount = 0

		

		self.stand  = []
		for i in range(1,5):
			self.stand.append(pygame.image.load('row-1-col-'+str(i)+'.png')) 
		self.walk  = []
		for i in range(1,5):
			self.walk.append(pygame.image.load('row-2-col-'+str(i)+'.png')) 
		self.dash  = []
		for i in range(1,4):
			self.dash.append(pygame.image.load('row-3-col-'+str(i)+'.png')) 
		self.backdash  = []
		for i in range(1,4):
			self.backdash.append(pygame.image.load('row-4-col-'+str(i)+'.png'))
		self.lightAttack  = []
		for j in range(22,25):
			for i in range(1,5):
				self.lightAttack.append(pygame.image.load('row-'+str(j)+'-col-'+str(i)+'.png')) 
		self.heavyAttack  = []
		for i in range(1,9):
			self.heavyAttack.append(pygame.image.load('row-25-col-'+str(i)+'.png'))   
		self.jump = []
		for i in range(6,9):
			self.jump.append(pygame.image.load('row-'+str(i)+'-col-1.png'))


		self.left = False
		self.right = False
		self.lock = False
		self.startTimer = False
		self.startPunchTimer = False
		self.startLTimer = False
		self.bdash = False
		self.fdash = False
		self.punchCount = 0
		self.heavyCount = 0
		self.timer = 0
		self.punchTimer = 0
		self.punch = False
		self.lightCombo1 = False
		self.lightCombo2 = False
		self.Ltimer = 0
		self.isJump = False
		self.jumpCount = -10
		self.heavy = False

	def redrawGameWindow(self):
	
		screen.blit(bg,(0,0))
		if self.walkCount + 1 > 4:
			self.walkCount = 0
		if self.standCount + 1 > 4:
			self.standCount = 0
		if self.punchCount + 1 > 12:
			self.punchCount = 0
		if self.jumpCount + 1 > 10:        
			self.jumpCount = -10


		if self.punch:
			screen.blit(self.lightAttack[self.punchCount],(self.x,self.y))
			self.punchCount += 1
			if self.punchCount % 4 == 0:
				self.lock = False
				self.punch = False
				self.punchTimer = 0
		elif self.heavy:
			screen.blit(self.heavyAttack[self.heavyCount],(self.x,self.y))
			self.heavyCount +=1 
			if self.heavyCount == 7:
				self.heavyCount = 0
				self.heavy = False
				self.lock = False


		elif self.left or self.right:
		
			screen.blit(self.walk[self.walkCount],(self.x,self.y)) 
			self.walkCount += 1

		elif self.bdash:
			for i in range(3):
				screen.blit(self.backdash[i],(self.x,self.y))
				self.x -= 20
			self.bdash = False

		elif self.fdash:
			for i in range(3):
				screen.blit(self.dash[i],(self.x,self.y))
				self.x += 20
			self.fdash = False

		elif self.isJump:
			if self.jumpCount == -10:
				screen.blit(self.jump[0],(self.x,self.y))
			
			elif self.jumpCount < 0:
				screen.blit(self.jump[1],(self.x,self.y))
				
			else:
				screen.blit(self.jump[2],(self.x,self.y))
				
			self.jumpCount += 1
			if self.jumpCount < 0:
				self.y -= (self.jumpCount**2) * 0.4
			else:
				self.y += (self.jumpCount**2) * 0.4
			if self.jumpCount == 9:
				self.jumpCount = -10
				self.isJump = False

			
		elif not self.punch:
			
			screen.blit(self.stand[self.standCount],(self.x,self.y))
			self.standCount += 1

		pygame.display.update()




player1 = character()

while not done:

	clock.tick(10)

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done = True
		
	keys = pygame.key.get_pressed()	
	
	#light attack b
	if keys[pygame.K_b] and not player1.lock:
	
						
						
						
								
		player1.lock = True
		player1.punch = True
		player1.startPunchTimer = True
		if player1.punchTimer > 5:
			
			player1.punchTimer = False
			player1.punchCount = 0


	#heavy attack n
	if keys[pygame.K_n] and not player1.lock:
		player1.lock = True
		player1.heavy = True
		
			

	#move Left 
	elif keys[pygame.K_LEFT] and player1.x > player1.speed-player1.width/2 and not player1.lock:
		if player1.isJump:
			player1.x -= player1.speed
		else:
			player1.startLTimer = True
			
			if 4 > player1.Ltimer >= 2 and player1.x > 20-player1.width/2:
				player1.startLTimer = False
				player1.Ltimer = 0
				
				player1.bdash = True

			else:
			
				player1.Ltimer = 0
				player1.x -= player1.speed
				player1.left = True
				player1.right = False
			
									
	#move right
	elif keys[pygame.K_RIGHT] and player1.x < 640 - player1.width - player1.speed and not player1.lock:
	
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


	if keys[pygame.K_SPACE] and not player1.isJump:
		player1.isJump = True




	else:
		player1.right = False
		player1.left = False
		player1.walkCount = 0
	if player1.startTimer:
		player1.timer += 1
	if player1.startPunchTimer:
		player1.punchTimer += 1
	if player1.startLTimer:
		player1.Ltimer += 1
		
	
	player1.redrawGameWindow()
pygame.quit()

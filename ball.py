import pygame
import math
from time import sleep
def play():

	pygame.init()
	screen=pygame.display.set_mode((600,600))
	pygame.display.set_caption('Ball')

	ballImg = pygame.image.load('ball.png')
	def ball(x,y):
		screen.blit(ballImg,(x,y))
	b_x=0
	b_y=0
	x_c=1.3
	y_c=0.7

	snowmanImg = pygame.image.load("snowman.png")
	def snowman(x,y):
		screen.blit(snowmanImg,(x,y))
	s_x=536
	s_y=536
	s_x_c=0
	s_y_c=0

	def isCollision(x1,y1,x2,y2):
		d=math.sqrt( math.pow(x2-x1 ,2) + math.pow(y2-y1,2))
		if d<64:
			return True
		else :
			return False

	score_value = 0
	font = pygame.font.Font('freesansbold.ttf', 32)
	textX = 10
	testY = 10

	def show_score(x, y):
	    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
	    screen.blit(score, (x, y))

	running=True
	while running:
		screen.fill((0,0,0))
		
		for e in pygame.event.get():
			if e.type ==pygame.QUIT:
				running = False
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_LEFT:
					s_x_c=-2
				elif e.key == pygame.K_RIGHT:
					s_x_c=2
			if e.type == pygame.KEYUP:
				if e.key in [pygame.K_LEFT,pygame.K_RIGHT]:
					s_x_c=0
		
		snowman(s_x,s_y)
		s_x+=s_x_c
		if s_x<=0:
			s_x=0
		elif s_x>=536:
			s_x=536
		ball(b_x,b_y)
		b_x+=x_c
		b_y+=y_c
		if b_y>=536:
			running=False
		if b_x>=536:
			x_c = -1.3		
		if b_y<=0:
			y_c = 0.7		
		if b_x<=0:
			x_c = 1.3
		if isCollision(s_x,s_y,b_x,b_y):
			y_c = -0.7
		score_value+=1
		show_score(textX, testY)
		pygame.display.update()
	font1 = pygame.font.Font('freesansbold.ttf', 100)
	gameover = font1.render("GameOver", True, (255, 255, 255))
	screen.blit(gameover, (40, 200))
	pygame.display.update()
	sleep(2)	
	pygame.quit()
play()

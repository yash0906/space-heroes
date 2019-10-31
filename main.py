import pygame
import sys
import random 
from pygame.locals import *
from time import sleep
class Character(object):
	def __init__(self,x,y,path):
		self.x_pos = x
		self.y_pos = y
		self.obj = pygame.image.load(path)
	def draw(self, screen):
		screen.blit(self.obj, (self.x_pos, self.y_pos))

class Ship(Character):
	def __init__(self,x,y,path):
		super().__init__(x,y,path)
	def moveright(self):
		self.x_pos += 10
	def moveleft(self):
		self.x_pos -= 10
	def moveup(self):
		self.y_pos-=10
	def movedown(self):
		self.y_pos += 10
	def nomove(self):
		self.x_pos +=0
		self.y_pos +=0
class Bullet(Character):
	def __init__(self,x,y,path):
		super().__init__(x,y,path)
sc_height = 500
sc_width = 500

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((sc_height, sc_width))
pygame.display.set_caption('Space Heroes')
sship = Ship(400,400,'/home/yash/room/game/ship.png')
run = True
bullets  = []
while run:
	clock.tick(20)
	screen.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE and len(bullets)<5:
				bullets.append(Bullet(sship.x_pos, sship.y_pos, '/home/yash/room/game/bullet2.png'))
	keys = pygame.key.get_pressed()  
	if keys[pygame.K_UP] and sship.y_pos>=0:
		sship.moveup()
	if keys[pygame.K_DOWN] and sship.y_pos<=410:
		sship.movedown()
	if keys[pygame.K_LEFT] and sship.x_pos>=10:
		sship.moveleft()
	if keys[pygame.K_RIGHT] and sship.x_pos<=410:
		sship.moveright()  
	for bul in bullets:
		if bul.y_pos<0:
			bullets.remove(bul)
			del bul
		else:
			bul.y_pos-=20
			bul.draw(screen)

	sship.draw(screen)
	pygame.display.flip()
pygame.quit()
quit()


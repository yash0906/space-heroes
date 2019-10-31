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
class Enemy(Character):
	def __init__(self,x,y,path):
		super().__init__(x,y,path)
	def moveforward(self):
		self.y_pos += 10
sc_height = 500
sc_width = 500
ship_height =  76
ship_widht = 71
bullet_height = 60
bullet_width = 60
enemy_height = 90
enemy_width = 90
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((sc_height, sc_width))
pygame.display.set_caption('Space Heroes')
sship = Ship(400,400,'/home/yash/room/game/space-heroes/ship.png')
bullet_sound = pygame.mixer.Sound('bullet_sound.wav')
crash_sound = pygame.mixer.Sound('crash.wav')
backmusic = pygame.mixer.music.load('backmusic.mp3')
blast = pygame.image.load('blast.jpg')
run = True
pygame.mixer.music.play(-1)
bullets  = []
enemies = []
background = pygame.image.load('space.jpg')
current_time = pygame.time.get_ticks()
final_time = pygame.time.get_ticks()
while run:
	clock.tick(20)
	current_time = pygame.time.get_ticks()
	screen.fill((0,0,0))
	screen.blit(background,(0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == K_SPACE and len(bullets)<5:
				bullets.append(Bullet(sship.x_pos, sship.y_pos, '/home/yash/room/game/space-heroes/bullet2.png'))
				bullet_sound.play()

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
	if current_time - final_time > 3000:
		final_time = current_time
		if len(enemies) < 3:
			enemies.append(Enemy(random.randint(0,410), 0, '/home/yash/room/game/space-heroes/enemy.png'))
	for ene in enemies:
		for bul in bullets:
			if bul.x_pos + bullet_width/2 >= ene.x_pos and bul.x_pos + bullet_width/2 <= (ene.x_pos + enemy_width) and bul.y_pos+40 <= (ene.y_pos+enemy_height) and bul.y_pos >= ene.y_pos :
				bullets.remove(bul)
				enemies.remove(ene)
				crash_sound.play()
				screen.blit(blast, (ene.x_pos,ene.y_pos))
				del ene
				del bul 
				break
	for ene in enemies:
		ene.moveforward()
		if ene.y_pos + enemy_height/2 > 500 :
			enemies.remove(ene)
			del ene
			continue
		ene.draw(screen)
	sship.draw(screen)
	pygame.display.flip()
pygame.quit()
quit()
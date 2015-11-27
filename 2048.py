import pygame
from pygame.locals import *
from sys import exit
from random import randint

#white_color = (255,255,255)
win_size = (400,400)
win_back = (183,175,156)
rec_size = (80,80)
rec_sep = 16
rec_color = {0:(204,192,176),2:(239,228,217),4:(236,225,198),8:(249,175,115),16:(255,142,90),32:(255,109,83),64:(255,66,32),128:(238,212,111),256:(239,211,95),512:(255,236,139),1024:(255,255,0),2048:(255,193,37),4096:(255,140,0)}
border_size = (4,4)
border = [[0 for i in xrange(border_size[0])] for j in xrange(border_size[1])]

pygame.init()
game_font = pygame.font.SysFont("arial",32)
screen = pygame.display.set_mode(win_size,0,32)
screen.fill(win_back)
pygame.display.update()

def check_lose():
	global border
	for item in border:
		for sub_item in item:
			if sub_item == 0:
				return False
	return True

#display border
def display():
	#global variable
	global border
	global rec_size
	global rec_sep
	global rec_color
	global game_font
	if not check_lose():
		for i,item in enumerate(border):
			for j,sub_item in enumerate(item):
				y = i*(rec_size[1] + rec_sep) + rec_sep
				x = j*(rec_size[0] + rec_sep) + rec_sep
				pygame.draw.rect(screen,rec_color[border[i][j]],((x,y),rec_size))
				if border[i][j] != 0:
					surface = game_font.render(str(border[i][j]),True,(255,255,255))	
					screen.blit(surface,(x+(rec_size[0]-surface.get_width())/2,y+(rec_size[1]-surface.get_height())/2))
		pygame.display.update()

#random a new 2
def rand_2(x = 1):
	global border
	global border_size
	x = randint(0,border_size[0]-1)
	y = randint(0,border_size[1]-1)
	while border[x][y] != 0:
		x = randint(0,border_size[0]-1)
		y = randint(0,border_size[1]-1)
	if x == 1:
		border[x][y] = 2
	else:
		if randint(1,100)>20:
			border[x][y] = 2
		else:
			border[x][y] = 4

def init_border():
	for i in xrange(2):
		rand_2()

def up():
	global border
	global border_size
	for i in xrange(border_size[0]):
		tmp = 0
		for j in xrange(1,border_size[1]):
			if border[j][i] == 0:
					continue

			if border[tmp][i] == 0:
				border[tmp][i] = border[j][i]
				border[j][i] = 0
			else:
				if border[j][i] == border[tmp][i]:
					border[tmp][i] *= 2
					border[j][i] = 0
				else:
					tmp += 1
					border[tmp][i] = border[j][i]
					if tmp != j:
						border[j][i] = 0

def down():
	global border
	global border_size
	for i in xrange(border_size[0]):
		tmp = border_size[1]-1
		for j in xrange(border_size[1]-2,-1,-1):
			if border[j][i] == 0:
					continue

			if border[tmp][i] == 0:
				border[tmp][i] = border[j][i]
				border[j][i] = 0
			else:
				if border[j][i] == border[tmp][i]:
					border[tmp][i] *= 2
					border[j][i] = 0
				else:
					tmp -= 1
					border[tmp][i] = border[j][i]
					if tmp != j:
						border[j][i] = 0

def right():
	global border
	global border_size
	for i in xrange(border_size[1]):
		tmp = border_size[0]-1
		for j in xrange(border_size[0]-2,-1,-1):
			if border[i][j] == 0:
					continue

			if border[i][tmp] == 0:
				border[i][tmp] = border[i][j]
				border[i][j] = 0
			else:
				if border[i][j] == border[i][tmp]:
					border[i][tmp] *= 2
					border[i][j] = 0
				else:
					tmp -= 1
					border[i][tmp] = border[i][j]
					if tmp != j:
						border[i][j] = 0

def left():
	global border
	global border_size
	for i in xrange(border_size[1]):
		tmp = 0
		for j in xrange(1,border_size[0]):
			if border[i][j] == 0:
					continue

			if border[i][tmp] == 0:
				border[i][tmp] = border[i][j]
				border[i][j] = 0
			else:
				if border[i][j] == border[i][tmp]:
					border[i][tmp] *= 2
					border[i][j] = 0
				else:
					tmp += 1
					border[i][tmp] = border[i][j]
					if tmp != j:
						border[i][j] = 0

init_border()
display()

while True:
	for event in pygame.event.get():
		#quit event
		if event.type == QUIT:
			exit()
		#if event.type == MOUSEBUTTONDOWN:
			#screen.fill(white_color)
			#pygame.draw.rect(screen,(111,222,121),((0,0),rec_size))
			#display()
			#pass
		elif event.type == KEYDOWN:	
			if event.key == K_LEFT:
				print("left")
                		left()
				display()
            		elif event.key == K_RIGHT:
				print("right")
                		right()
				display()
            		elif event.key == K_UP:
				print("up")
                		up()
				display()
            		elif event.key == K_DOWN:
				print("down")
               			down()
				display()
			rand_2(2)
			display()

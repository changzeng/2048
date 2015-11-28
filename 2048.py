import pygame
from pygame.locals import *
from sys import exit
from random import randint
from copy import deepcopy as deepcp
from time import sleep

#white_color = (255,255,255)
win_size = (400,400)
win_back = (183,175,156)
rec_size = (80,80)
rec_sep = 16
rec_color = {0:(204,192,176),2:(239,228,217),4:(236,225,198),8:(249,175,115),16:(255,142,90),32:(255,109,83),64:(255,66,32),128:(238,212,111),256:(239,211,95),512:(255,236,139),1024:(255,255,0),2048:(255,193,37),4096:(255,140,0)}

pygame.init()
game_font = pygame.font.SysFont("arial",32)
screen = pygame.display.set_mode(win_size,0,32)
#initialize screen color	
screen.fill(win_back)
pygame.display.update()


class AI_2048():
	def __init__(self,size):
		self.border_size = size
		self.border = [[0 for i in xrange(self.border_size[0])] for j in xrange(self.border_size[1])]
		for i in xrange(2):
			self.rand_2()

	#check if border has free room
	def check_lose(self):
		for item in self.border:
			for sub_item in item:
				if sub_item == 0:
					return False
		return True

	#display border
	def display(self):
		#global variable
		global screen
		global rec_size
		global rec_sep
		global rec_color
		global game_font
		for i,item in enumerate(self.border):
			for j,sub_item in enumerate(item):
				y = i*(rec_size[1] + rec_sep) + rec_sep
				x = j*(rec_size[0] + rec_sep) + rec_sep
				pygame.draw.rect(screen,rec_color[self.border[i][j]],((x,y),rec_size))
				if self.border[i][j] != 0:
					if self.border[i][j] == 2 or self.border[i][j] == 4:
						surface = game_font.render(str(self.border[i][j]),True,(124,115,105))
					else:
						surface = game_font.render(str(self.border[i][j]),True,(255,255,255))	
					screen.blit(surface,(x+(rec_size[0]-surface.get_width())/2,y+(rec_size[1]-surface.get_height())/2))
		pygame.display.update()

	#random a new 2 or 4
	def rand_2(self,arg = 1):
		tmp_list = []
		for i in xrange(self.border_size[1]):
			for j in xrange(self.border_size[0]):
				if self.border[i][j] == 0:
					tmp_list.append((i,j))
		if len(tmp_list) == 0:
			return
		i = randint(0,len(tmp_list)-1)
		x = tmp_list[i][0]
		y = tmp_list[i][1]
		if arg == 1:
			self.border[x][y] = 2
		else:
			if randint(1,100)>20:
				self.border[x][y] = 2
			else:
				self.border[x][y] = 4

	def genera_identity(self):
		s = ""
		for item in self.border:
			for sub_item in item:
				s += str(sub_item)
		return s

	def up(self):
		for i in xrange(self.border_size[0]):
			tmp = 0
			for j in xrange(1,self.border_size[1]):
				if self.border[j][i] == 0:
						continue

				if self.border[tmp][i] == 0:
					self.border[tmp][i] = self.border[j][i]
					self.border[j][i] = 0
				else:
					if self.border[j][i] == self.border[tmp][i]:
						self.border[tmp][i] *= 2
						self.border[j][i] = 0
					else:
						tmp += 1
						self.border[tmp][i] = self.border[j][i]
						if tmp != j:
							self.border[j][i] = 0

	def down(self):
		for i in xrange(self.border_size[0]):
			tmp = self.border_size[1]-1
			for j in xrange(self.border_size[1]-2,-1,-1):
				if self.border[j][i] == 0:
						continue

				if self.border[tmp][i] == 0:
					self.border[tmp][i] = self.border[j][i]
					self.border[j][i] = 0
				else:
					if self.border[j][i] == self.border[tmp][i]:
						self.border[tmp][i] *= 2
						self.border[j][i] = 0
					else:
						tmp -= 1
						self.border[tmp][i] = self.border[j][i]
						if tmp != j:
							self.border[j][i] = 0

	def right(self):
		for i in xrange(self.border_size[1]):
			tmp = self.border_size[0]-1
			for j in xrange(self.border_size[0]-2,-1,-1):
				if self.border[i][j] == 0:
						continue

				if self.border[i][tmp] == 0:
					self.border[i][tmp] = self.border[i][j]
					self.border[i][j] = 0
				else:
					if self.border[i][j] == self.border[i][tmp]:
						self.border[i][tmp] *= 2
						self.border[i][j] = 0
					else:
						tmp -= 1
						self.border[i][tmp] = self.border[i][j]
						if tmp != j:
							self.border[i][j] = 0

	def left(self):
		for i in xrange(self.border_size[1]):
			tmp = 0
			for j in xrange(1,self.border_size[0]):
				if self.border[i][j] == 0:
						continue

				if self.border[i][tmp] == 0:
					self.border[i][tmp] = self.border[i][j]
					self.border[i][j] = 0
				else:
					if self.border[i][j] == self.border[i][tmp]:
						self.border[i][tmp] *= 2
						self.border[i][j] = 0
					else:
						tmp += 1
						self.border[i][tmp] = self.border[i][j]
						if tmp != j:
							self.border[i][j] = 0
	def cal_zero_num(self):
		num = 0
		for item in self.border:
			for sub_item in item:
				if sub_item == 0:
					num += 1
		return num
	
	def cal_sum(self):
		num = 0
		for item in self.border:
			num += sum(item)

		return num
	def move(self,arg):
		if arg == 1:
			self.up()
		elif arg == 2:
			self.down()
		elif arg == 3:
			self.right()
		elif arg == 4:
			self.left()
		self.display()

def make_dicision(arg):
	up_cp = deepcp(arg)
	down_cp = deepcp(arg)
	right_cp = deepcp(arg)
	left_cp = deepcp(arg)
	cp_list = [up_cp,down_cp,right_cp,left_cp]
	up_cp.up()
	down_cp.down()
	right_cp.right()
	left_cp.left()
	gene_identity = arg.genera_identity()
	zero_num = 0
	dire = 0

	for index,item in enumerate(cp_list):
		if item.genera_identity() != gene_identity:
			zero_tmp = item.cal_zero_num()
			if zero_tmp > zero_num:
				zero_num = zero_tmp
				dire = index + 1
	#num_list = [up_cp.cal_zero_num(),down_cp.cal_zero_num(),right_cp.cal_zero_num(),left_cp.cal_zero_num()]
	#print(num_list)	
	#return num_list.index(max(num_list))+1
	#sum_list = [up_cp.cal_sum(),down_cp.cal_sum(),right_cp.cal_sum(),left_cp.cal_sum()]
	#max_sum = max(sum_list)
	#sub_cp_list = cp_list[max_sum:max_sum + sum_list.count(max_sum)]

	return dire

a2048 = AI_2048((4,4))
a2048.display()


while True:
	dire = make_dicision(a2048)
	s1 = a2048.genera_identity()
	a2048.move(dire)
	s2 = a2048.genera_identity()
	if s1 != s2:
		a2048.rand_2(2)
	a2048.display()
	print(dire)
	sleep(0.1)

'''
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
				s1 = a2048.genera_identity()
                		a2048.left()
				s2 = a2048.genera_identity()
				a2048.display()
				if s1 != s2:
					a2048.rand_2(2)
					a2048.display()
            		elif event.key == K_RIGHT:
				print("right")
				s1 = a2048.genera_identity()
                		a2048.right()
				s2 = a2048.genera_identity()
				a2048.display()
				if s1 != s2:
					a2048.rand_2(2)
					a2048.display()
			elif event.key == K_UP:
				print("up")
				s1 = a2048.genera_identity()
                		a2048.up()
				s2 = a2048.genera_identity()
				a2048.display()
				if s1 != s2:
					a2048.rand_2(2)
					a2048.display()
            		elif event.key == K_DOWN:
				print("down")
				s1 = a2048.genera_identity()
                		a2048.down()
				s2 = a2048.genera_identity()
				a2048.display()
				if s1 != s2:
					a2048.rand_2(2)
					a2048.display()
'''

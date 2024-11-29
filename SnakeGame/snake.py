import pygame,sys,random
from pygame.math import Vector2
from button import Button
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 30

SCREEN_WIDTH=cell_number*cell_size
SCREEN_HEIGHT=cell_number*8//13*cell_size

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

apple = pygame.image.load('Graphics/apple.png').convert_alpha()
mushroom=pygame.image.load('Graphics/poison.png').convert_alpha()
game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 25)

class SNAKE:
	def __init__(self,skin):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(1,0)
		self.new_block = False
		self.save_direction =	Vector2(1,0)
		self.minus_block = False
		self.hit_block = False
		self.second_flash=0
		self.skin=skin
 		#Chỉ số tốc độ của snake
		self.snake_speed = 3

		if self.skin==0:
			self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
			self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
			self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
			self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
			
			self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
			self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
			self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
			self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

			self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
			self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

			self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
			self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
			self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
			self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
			self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
	# hit
			self.head_up_hit = pygame.image.load('Graphics/head_up_hit.png').convert_alpha()
			self.head_down_hit = pygame.image.load('Graphics/head_down_hit.png').convert_alpha()
			self.head_right_hit = pygame.image.load('Graphics/head_right_hit.png').convert_alpha()
			self.head_left_hit = pygame.image.load('Graphics/head_left_hit.png').convert_alpha()
			
			self.tail_up_hit = pygame.image.load('Graphics/tail_up_hit.png').convert_alpha()
			self.tail_down_hit = pygame.image.load('Graphics/tail_down_hit.png').convert_alpha()
			self.tail_right_hit = pygame.image.load('Graphics/tail_right_hit.png').convert_alpha()
			self.tail_left_hit = pygame.image.load('Graphics/tail_left_hit.png').convert_alpha()

			self.body_vertical_hit = pygame.image.load('Graphics/body_vertical_hit.png').convert_alpha()
			self.body_horizontal_hit = pygame.image.load('Graphics/body_horizontal_hit.png').convert_alpha()

			self.body_tr_hit = pygame.image.load('Graphics/body_tr_hit.png').convert_alpha()
			self.body_tl_hit = pygame.image.load('Graphics/body_tl_hit.png').convert_alpha()
			self.body_br_hit = pygame.image.load('Graphics/body_br_hit.png').convert_alpha()
			self.body_bl_hit = pygame.image.load('Graphics/body_bl_hit.png').convert_alpha()
	# stun
			self.head_up_stun = pygame.image.load('Graphics/stun_head_up.png').convert_alpha()
			self.head_down_stun = pygame.image.load('Graphics/stun_head_down.png').convert_alpha()
			self.head_right_stun = pygame.image.load('Graphics/stun_head_right.png').convert_alpha()
			self.head_left_stun = pygame.image.load('Graphics/stun_head_left.png').convert_alpha()
			
			self.tail_up_stun = pygame.image.load('Graphics/tail_up.png').convert_alpha()
			self.tail_down_stun = pygame.image.load('Graphics/tail_down.png').convert_alpha()
			self.tail_right_stun = pygame.image.load('Graphics/tail_right.png').convert_alpha()
			self.tail_left_stun = pygame.image.load('Graphics/tail_left.png').convert_alpha()

			self.body_vertical_stun = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
			self.body_horizontal_stun = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

			self.body_tr_stun = pygame.image.load('Graphics/body_tr.png').convert_alpha()
			self.body_tl_stun = pygame.image.load('Graphics/body_tl.png').convert_alpha()
			self.body_br_stun = pygame.image.load('Graphics/body_br.png').convert_alpha()
			self.body_bl_stun = pygame.image.load('Graphics/body_bl.png').convert_alpha()
	# stun hit
			self.head_up_stun_hit = pygame.image.load('Graphics/stun_head_up_hit.png').convert_alpha()
			self.head_down_stun_hit = pygame.image.load('Graphics/stun_head_down_hit.png').convert_alpha()
			self.head_right_stun_hit = pygame.image.load('Graphics/stun_head_right_hit.png').convert_alpha()
			self.head_left_stun_hit = pygame.image.load('Graphics/stun_head_left_hit.png').convert_alpha()
			
			self.tail_up_stun_hit = pygame.image.load('Graphics/tail_up_hit.png').convert_alpha()
			self.tail_down_stun_hit = pygame.image.load('Graphics/tail_down_hit.png').convert_alpha()
			self.tail_right_stun_hit = pygame.image.load('Graphics/tail_right_hit.png').convert_alpha()
			self.tail_left_stun_hit = pygame.image.load('Graphics/tail_left_hit.png').convert_alpha()

			self.body_vertical_stun_hit = pygame.image.load('Graphics/body_vertical_hit.png').convert_alpha()
			self.body_horizontal_stun_hit = pygame.image.load('Graphics/body_horizontal_hit.png').convert_alpha()

			self.body_tr_stun_hit = pygame.image.load('Graphics/body_tr_hit.png').convert_alpha()
			self.body_tl_stun_hit = pygame.image.load('Graphics/body_tl_hit.png').convert_alpha()
			self.body_br_stun_hit = pygame.image.load('Graphics/body_br_hit.png').convert_alpha()
			self.body_bl_stun_hit = pygame.image.load('Graphics/body_bl_hit.png').convert_alpha()
		elif self.skin==1:
			self.head_up = pygame.image.load('Graphics/dragon_head_up.png').convert_alpha()
			self.head_down = pygame.image.load('Graphics/dragon_head_down.png').convert_alpha()
			self.head_right = pygame.image.load('Graphics/dragon_head_right.png').convert_alpha()
			self.head_left = pygame.image.load('Graphics/dragon_head_left.png').convert_alpha()
			
			self.tail_up = pygame.image.load('Graphics/dragon_tail_up.png').convert_alpha()
			self.tail_down = pygame.image.load('Graphics/dragon_tail_down.png').convert_alpha()
			self.tail_right = pygame.image.load('Graphics/dragon_tail_right.png').convert_alpha()
			self.tail_left = pygame.image.load('Graphics/dragon_tail_left.png').convert_alpha()

			self.body_vertical = pygame.image.load('Graphics/dragon_body_vertical.png').convert_alpha()
			self.body_horizontal = pygame.image.load('Graphics/dragon_body_horizontal.png').convert_alpha()

			self.body_tr = pygame.image.load('Graphics/dragon_body_tr.png').convert_alpha()
			self.body_tl = pygame.image.load('Graphics/dragon_body_tl.png').convert_alpha()
			self.body_br = pygame.image.load('Graphics/dragon_body_br.png').convert_alpha()
			self.body_bl = pygame.image.load('Graphics/dragon_body_bl.png').convert_alpha()
			self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
	# hit
			self.head_up_hit = pygame.image.load('Graphics/dragon_head_up_hit.png').convert_alpha()
			self.head_down_hit = pygame.image.load('Graphics/dragon_head_down_hit.png').convert_alpha()
			self.head_right_hit = pygame.image.load('Graphics/dragon_head_right_hit.png').convert_alpha()
			self.head_left_hit = pygame.image.load('Graphics/dragon_head_left_hit.png').convert_alpha()
			
			self.tail_up_hit = pygame.image.load('Graphics/dragon_tail_up_hit.png').convert_alpha()
			self.tail_down_hit = pygame.image.load('Graphics/dragon_tail_down_hit.png').convert_alpha()
			self.tail_right_hit = pygame.image.load('Graphics/dragon_tail_right_hit.png').convert_alpha()
			self.tail_left_hit = pygame.image.load('Graphics/dragon_tail_left_hit.png').convert_alpha()

			self.body_vertical_hit = pygame.image.load('Graphics/dragon_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_hit = pygame.image.load('Graphics/dragon_body_horizontal_hit.png').convert_alpha()

			self.body_tr_hit = pygame.image.load('Graphics/dragon_body_tr_hit.png').convert_alpha()
			self.body_tl_hit = pygame.image.load('Graphics/dragon_body_tl_hit.png').convert_alpha()
			self.body_br_hit = pygame.image.load('Graphics/dragon_body_br_hit.png').convert_alpha()
			self.body_bl_hit = pygame.image.load('Graphics/dragon_body_bl_hit.png').convert_alpha()
	# stun
			self.head_up_stun = pygame.image.load('Graphics/stun_dragon_head_up.png').convert_alpha()
			self.head_down_stun = pygame.image.load('Graphics/stun_dragon_head_down.png').convert_alpha()
			self.head_right_stun = pygame.image.load('Graphics/stun_dragon_head_right.png').convert_alpha()
			self.head_left_stun = pygame.image.load('Graphics/stun_dragon_head_left.png').convert_alpha()
			
			self.tail_up_stun = pygame.image.load('Graphics/dragon_tail_up.png').convert_alpha()
			self.tail_down_stun = pygame.image.load('Graphics/dragon_tail_down.png').convert_alpha()
			self.tail_right_stun = pygame.image.load('Graphics/dragon_tail_right.png').convert_alpha()
			self.tail_left_stun = pygame.image.load('Graphics/dragon_tail_left.png').convert_alpha()

			self.body_vertical_stun = pygame.image.load('Graphics/dragon_body_vertical.png').convert_alpha()
			self.body_horizontal_stun = pygame.image.load('Graphics/dragon_body_horizontal.png').convert_alpha()

			self.body_tr_stun = pygame.image.load('Graphics/dragon_body_tr.png').convert_alpha()
			self.body_tl_stun = pygame.image.load('Graphics/dragon_body_tl.png').convert_alpha()
			self.body_br_stun = pygame.image.load('Graphics/dragon_body_br.png').convert_alpha()
			self.body_bl_stun = pygame.image.load('Graphics/dragon_body_bl.png').convert_alpha()
	# stun hit
			self.head_up_stun_hit = pygame.image.load('Graphics/stun_dragon_head_up_hit.png').convert_alpha()
			self.head_down_stun_hit = pygame.image.load('Graphics/stun_dragon_head_down_hit.png').convert_alpha()
			self.head_right_stun_hit = pygame.image.load('Graphics/stun_dragon_head_right_hit.png').convert_alpha()
			self.head_left_stun_hit = pygame.image.load('Graphics/stun_dragon_head_left_hit.png').convert_alpha()
			
			self.tail_up_stun_hit = pygame.image.load('Graphics/dragon_tail_up_hit.png').convert_alpha()
			self.tail_down_stun_hit = pygame.image.load('Graphics/dragon_tail_down_hit.png').convert_alpha()
			self.tail_right_stun_hit = pygame.image.load('Graphics/dragon_tail_right_hit.png').convert_alpha()
			self.tail_left_stun_hit = pygame.image.load('Graphics/dragon_tail_left_hit.png').convert_alpha()

			self.body_vertical_stun_hit = pygame.image.load('Graphics/dragon_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_stun_hit = pygame.image.load('Graphics/dragon_body_horizontal_hit.png').convert_alpha()

			self.body_tr_stun_hit = pygame.image.load('Graphics/dragon_body_tr_hit.png').convert_alpha()
			self.body_tl_stun_hit = pygame.image.load('Graphics/dragon_body_tl_hit.png').convert_alpha()
			self.body_br_stun_hit = pygame.image.load('Graphics/dragon_body_br_hit.png').convert_alpha()
			self.body_bl_stun_hit = pygame.image.load('Graphics/dragon_body_bl_hit.png').convert_alpha()
		elif self.skin==2:
			self.head_up = pygame.image.load('Graphics/ant_head_up.png').convert_alpha()
			self.head_down = pygame.image.load('Graphics/ant_head_down.png').convert_alpha()
			self.head_right = pygame.image.load('Graphics/ant_head_right.png').convert_alpha()
			self.head_left = pygame.image.load('Graphics/ant_head_left.png').convert_alpha()
			
			self.tail_up = pygame.image.load('Graphics/ant_tail_up.png').convert_alpha()
			self.tail_down = pygame.image.load('Graphics/ant_tail_down.png').convert_alpha()
			self.tail_right = pygame.image.load('Graphics/ant_tail_right.png').convert_alpha()
			self.tail_left = pygame.image.load('Graphics/ant_tail_left.png').convert_alpha()

			self.body_vertical = pygame.image.load('Graphics/ant_body_vertical.png').convert_alpha()
			self.body_horizontal = pygame.image.load('Graphics/ant_body_horizontal.png').convert_alpha()

			self.body_tr = pygame.image.load('Graphics/ant_body_tr.png').convert_alpha()
			self.body_tl = pygame.image.load('Graphics/ant_body_tl.png').convert_alpha()
			self.body_br = pygame.image.load('Graphics/ant_body_br.png').convert_alpha()
			self.body_bl = pygame.image.load('Graphics/ant_body_bl.png').convert_alpha()
			self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
	# hit
			self.head_up_hit = pygame.image.load('Graphics/ant_head_up_hit.png').convert_alpha()
			self.head_down_hit = pygame.image.load('Graphics/ant_head_down_hit.png').convert_alpha()
			self.head_right_hit = pygame.image.load('Graphics/ant_head_right_hit.png').convert_alpha()
			self.head_left_hit = pygame.image.load('Graphics/ant_head_left_hit.png').convert_alpha()
			
			self.tail_up_hit = pygame.image.load('Graphics/ant_tail_up_hit.png').convert_alpha()
			self.tail_down_hit = pygame.image.load('Graphics/ant_tail_down_hit.png').convert_alpha()
			self.tail_right_hit = pygame.image.load('Graphics/ant_tail_right_hit.png').convert_alpha()
			self.tail_left_hit = pygame.image.load('Graphics/ant_tail_left_hit.png').convert_alpha()

			self.body_vertical_hit = pygame.image.load('Graphics/ant_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_hit = pygame.image.load('Graphics/ant_body_horizontal_hit.png').convert_alpha()

			self.body_tr_hit = pygame.image.load('Graphics/ant_body_tr_hit.png').convert_alpha()
			self.body_tl_hit = pygame.image.load('Graphics/ant_body_tl_hit.png').convert_alpha()
			self.body_br_hit = pygame.image.load('Graphics/ant_body_br_hit.png').convert_alpha()
			self.body_bl_hit = pygame.image.load('Graphics/ant_body_bl_hit.png').convert_alpha()
	# stun
			self.head_up_stun = pygame.image.load('Graphics/stun_ant_head_up.png').convert_alpha()
			self.head_down_stun = pygame.image.load('Graphics/stun_ant_head_down.png').convert_alpha()
			self.head_right_stun = pygame.image.load('Graphics/stun_ant_head_right.png').convert_alpha()
			self.head_left_stun = pygame.image.load('Graphics/stun_ant_head_left.png').convert_alpha()
			
			self.tail_up_stun = pygame.image.load('Graphics/ant_tail_up.png').convert_alpha()
			self.tail_down_stun = pygame.image.load('Graphics/ant_tail_down.png').convert_alpha()
			self.tail_right_stun = pygame.image.load('Graphics/ant_tail_right.png').convert_alpha()
			self.tail_left_stun = pygame.image.load('Graphics/ant_tail_left.png').convert_alpha()

			self.body_vertical_stun = pygame.image.load('Graphics/ant_body_vertical.png').convert_alpha()
			self.body_horizontal_stun = pygame.image.load('Graphics/ant_body_horizontal.png').convert_alpha()

			self.body_tr_stun = pygame.image.load('Graphics/ant_body_tr.png').convert_alpha()
			self.body_tl_stun = pygame.image.load('Graphics/ant_body_tl.png').convert_alpha()
			self.body_br_stun = pygame.image.load('Graphics/ant_body_br.png').convert_alpha()
			self.body_bl_stun = pygame.image.load('Graphics/ant_body_bl.png').convert_alpha()
	# stun hit
			self.head_up_stun_hit = pygame.image.load('Graphics/stun_ant_head_up_hit.png').convert_alpha()
			self.head_down_stun_hit = pygame.image.load('Graphics/stun_ant_head_down_hit.png').convert_alpha()
			self.head_right_stun_hit = pygame.image.load('Graphics/stun_ant_head_right_hit.png').convert_alpha()
			self.head_left_stun_hit = pygame.image.load('Graphics/stun_ant_head_left_hit.png').convert_alpha()
			
			self.tail_up_stun_hit = pygame.image.load('Graphics/ant_tail_up_hit.png').convert_alpha()
			self.tail_down_stun_hit = pygame.image.load('Graphics/ant_tail_down_hit.png').convert_alpha()
			self.tail_right_stun_hit = pygame.image.load('Graphics/ant_tail_right_hit.png').convert_alpha()
			self.tail_left_stun_hit = pygame.image.load('Graphics/ant_tail_left_hit.png').convert_alpha()

			self.body_vertical_stun_hit = pygame.image.load('Graphics/ant_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_stun_hit = pygame.image.load('Graphics/ant_body_horizontal_hit.png').convert_alpha()

			self.body_tr_stun_hit = pygame.image.load('Graphics/ant_body_tr_hit.png').convert_alpha()
			self.body_tl_stun_hit = pygame.image.load('Graphics/ant_body_tl_hit.png').convert_alpha()
			self.body_br_stun_hit = pygame.image.load('Graphics/ant_body_br_hit.png').convert_alpha()
			self.body_bl_stun_hit = pygame.image.load('Graphics/ant_body_bl_hit.png').convert_alpha()
		
	def draw_snake(self):
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
			
			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def draw_snake_hit(self):
		self.update_head_graphics_hit()
		self.update_tail_graphics_hit()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical_hit,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal_hit,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl_hit,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br_hit,block_rect)

	def update_head_graphics_hit(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left_hit
		elif head_relation == Vector2(-1,0): self.head = self.head_right_hit
		elif head_relation == Vector2(0,1): self.head = self.head_up_hit
		elif head_relation == Vector2(0,-1): self.head = self.head_down_hit

	def update_tail_graphics_hit(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left_hit
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right_hit
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up_hit
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down_hit

	def draw_snake_stun(self):
		self.update_head_graphics_stun()
		self.update_tail_graphics_stun()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical_stun,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal_stun,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl_stun,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl_stun,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr_stun,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br_stun,block_rect)

	def update_head_graphics_stun(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left_stun
		elif head_relation == Vector2(-1,0): self.head = self.head_right_stun
		elif head_relation == Vector2(0,1): self.head = self.head_up_stun
		elif head_relation == Vector2(0,-1): self.head = self.head_down_stun

	def update_tail_graphics_stun(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left_stun
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right_stun
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up_stun
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down_stun

	def draw_snake_stun_hit(self):
		self.update_head_graphics_stun_hit()
		self.update_tail_graphics_stun_hit()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical_stun_hit,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal_stun_hit,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl_stun_hit,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl_stun_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr_stun_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br_stun_hit,block_rect)

	def update_head_graphics_stun_hit(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left_stun_hit
		elif head_relation == Vector2(-1,0): self.head = self.head_right_stun_hit
		elif head_relation == Vector2(0,1): self.head = self.head_up_stun_hit
		elif head_relation == Vector2(0,-1): self.head = self.head_down_stun_hit

	def update_tail_graphics_stun_hit(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left_stun_hit
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right_stun_hit
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up_stun_hit
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down_stun_hit

	def move_snake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

	def minus_snake(self):
		if self.minus_block == True:
			body_copy = self.body[:-2]
			self.body = body_copy[:]
			self.minus_block = False

	def play_crunch_sound(self):
		self.crunch_sound.play()

	def reset(self):
		self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
		self.direction = Vector2(1,0)
		self.save_direction = Vector2(1,0)
  
	#Chỉ số tốc độ tăng lên khi đủ điểm
	def increase_speed(self):
		self.snake_speed += 2.5
		print("Snake speed : ",self.snake_speed)

	#Thiết lập thêm hàm speed cho chế độ
	def get_snake_speed(self):
		return self.snake_speed
class SNAKE2:
	def __init__(self,skin):
		self.body = [Vector2(cell_number-7, 10), Vector2(cell_number-6, 10), Vector2(cell_number-5, 10)]
		self.direction = Vector2(-1,0)
		self.new_block = False
		self.save_direction =	Vector2(-1,0)
		self.minus_block = False	
		self.hit_block = False
		self.second_flash=0
		self.skin = 2
		if skin > 0: 
			self.skin = skin - 1

 		#Chỉ số tốc độ của snake
		self.snake_speed = 3

		if self.skin==0:
			self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
			self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
			self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()
			self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
			
			self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
			self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
			self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()
			self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()

			self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
			self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

			self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
			self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
			self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
			self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
			self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
	# hit
			self.head_up_hit = pygame.image.load('Graphics/head_up_hit.png').convert_alpha()
			self.head_down_hit = pygame.image.load('Graphics/head_down_hit.png').convert_alpha()
			self.head_right_hit = pygame.image.load('Graphics/head_right_hit.png').convert_alpha()
			self.head_left_hit = pygame.image.load('Graphics/head_left_hit.png').convert_alpha()
			
			self.tail_up_hit = pygame.image.load('Graphics/tail_up_hit.png').convert_alpha()
			self.tail_down_hit = pygame.image.load('Graphics/tail_down_hit.png').convert_alpha()
			self.tail_right_hit = pygame.image.load('Graphics/tail_right_hit.png').convert_alpha()
			self.tail_left_hit = pygame.image.load('Graphics/tail_left_hit.png').convert_alpha()

			self.body_vertical_hit = pygame.image.load('Graphics/body_vertical_hit.png').convert_alpha()
			self.body_horizontal_hit = pygame.image.load('Graphics/body_horizontal_hit.png').convert_alpha()

			self.body_tr_hit = pygame.image.load('Graphics/body_tr_hit.png').convert_alpha()
			self.body_tl_hit = pygame.image.load('Graphics/body_tl_hit.png').convert_alpha()
			self.body_br_hit = pygame.image.load('Graphics/body_br_hit.png').convert_alpha()
			self.body_bl_hit = pygame.image.load('Graphics/body_bl_hit.png').convert_alpha()
	# stun
			self.head_up_stun = pygame.image.load('Graphics/stun_head_up.png').convert_alpha()
			self.head_down_stun = pygame.image.load('Graphics/stun_head_down.png').convert_alpha()
			self.head_right_stun = pygame.image.load('Graphics/stun_head_right.png').convert_alpha()
			self.head_left_stun = pygame.image.load('Graphics/stun_head_left.png').convert_alpha()
			
			self.tail_up_stun = pygame.image.load('Graphics/tail_up.png').convert_alpha()
			self.tail_down_stun = pygame.image.load('Graphics/tail_down.png').convert_alpha()
			self.tail_right_stun = pygame.image.load('Graphics/tail_right.png').convert_alpha()
			self.tail_left_stun = pygame.image.load('Graphics/tail_left.png').convert_alpha()

			self.body_vertical_stun = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
			self.body_horizontal_stun = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

			self.body_tr_stun = pygame.image.load('Graphics/body_tr.png').convert_alpha()
			self.body_tl_stun = pygame.image.load('Graphics/body_tl.png').convert_alpha()
			self.body_br_stun = pygame.image.load('Graphics/body_br.png').convert_alpha()
			self.body_bl_stun = pygame.image.load('Graphics/body_bl.png').convert_alpha()
	# stun hit
			self.head_up_stun_hit = pygame.image.load('Graphics/stun_head_up_hit.png').convert_alpha()
			self.head_down_stun_hit = pygame.image.load('Graphics/stun_head_down_hit.png').convert_alpha()
			self.head_right_stun_hit = pygame.image.load('Graphics/stun_head_right_hit.png').convert_alpha()
			self.head_left_stun_hit = pygame.image.load('Graphics/stun_head_left_hit.png').convert_alpha()
			
			self.tail_up_stun_hit = pygame.image.load('Graphics/tail_up_hit.png').convert_alpha()
			self.tail_down_stun_hit = pygame.image.load('Graphics/tail_down_hit.png').convert_alpha()
			self.tail_right_stun_hit = pygame.image.load('Graphics/tail_right_hit.png').convert_alpha()
			self.tail_left_stun_hit = pygame.image.load('Graphics/tail_left_hit.png').convert_alpha()

			self.body_vertical_stun_hit = pygame.image.load('Graphics/body_vertical_hit.png').convert_alpha()
			self.body_horizontal_stun_hit = pygame.image.load('Graphics/body_horizontal_hit.png').convert_alpha()

			self.body_tr_stun_hit = pygame.image.load('Graphics/body_tr_hit.png').convert_alpha()
			self.body_tl_stun_hit = pygame.image.load('Graphics/body_tl_hit.png').convert_alpha()
			self.body_br_stun_hit = pygame.image.load('Graphics/body_br_hit.png').convert_alpha()
			self.body_bl_stun_hit = pygame.image.load('Graphics/body_bl_hit.png').convert_alpha()
		elif self.skin==1:
			self.head_up = pygame.image.load('Graphics/dragon_head_up.png').convert_alpha()
			self.head_down = pygame.image.load('Graphics/dragon_head_down.png').convert_alpha()
			self.head_right = pygame.image.load('Graphics/dragon_head_right.png').convert_alpha()
			self.head_left = pygame.image.load('Graphics/dragon_head_left.png').convert_alpha()
			
			self.tail_up = pygame.image.load('Graphics/dragon_tail_up.png').convert_alpha()
			self.tail_down = pygame.image.load('Graphics/dragon_tail_down.png').convert_alpha()
			self.tail_right = pygame.image.load('Graphics/dragon_tail_right.png').convert_alpha()
			self.tail_left = pygame.image.load('Graphics/dragon_tail_left.png').convert_alpha()

			self.body_vertical = pygame.image.load('Graphics/dragon_body_vertical.png').convert_alpha()
			self.body_horizontal = pygame.image.load('Graphics/dragon_body_horizontal.png').convert_alpha()

			self.body_tr = pygame.image.load('Graphics/dragon_body_tr.png').convert_alpha()
			self.body_tl = pygame.image.load('Graphics/dragon_body_tl.png').convert_alpha()
			self.body_br = pygame.image.load('Graphics/dragon_body_br.png').convert_alpha()
			self.body_bl = pygame.image.load('Graphics/dragon_body_bl.png').convert_alpha()
			self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
	# hit
			self.head_up_hit = pygame.image.load('Graphics/dragon_head_up_hit.png').convert_alpha()
			self.head_down_hit = pygame.image.load('Graphics/dragon_head_down_hit.png').convert_alpha()
			self.head_right_hit = pygame.image.load('Graphics/dragon_head_right_hit.png').convert_alpha()
			self.head_left_hit = pygame.image.load('Graphics/dragon_head_left_hit.png').convert_alpha()
			
			self.tail_up_hit = pygame.image.load('Graphics/dragon_tail_up_hit.png').convert_alpha()
			self.tail_down_hit = pygame.image.load('Graphics/dragon_tail_down_hit.png').convert_alpha()
			self.tail_right_hit = pygame.image.load('Graphics/dragon_tail_right_hit.png').convert_alpha()
			self.tail_left_hit = pygame.image.load('Graphics/dragon_tail_left_hit.png').convert_alpha()

			self.body_vertical_hit = pygame.image.load('Graphics/dragon_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_hit = pygame.image.load('Graphics/dragon_body_horizontal_hit.png').convert_alpha()

			self.body_tr_hit = pygame.image.load('Graphics/dragon_body_tr_hit.png').convert_alpha()
			self.body_tl_hit = pygame.image.load('Graphics/dragon_body_tl_hit.png').convert_alpha()
			self.body_br_hit = pygame.image.load('Graphics/dragon_body_br_hit.png').convert_alpha()
			self.body_bl_hit = pygame.image.load('Graphics/dragon_body_bl_hit.png').convert_alpha()
	# stun
			self.head_up_stun = pygame.image.load('Graphics/stun_dragon_head_up.png').convert_alpha()
			self.head_down_stun = pygame.image.load('Graphics/stun_dragon_head_down.png').convert_alpha()
			self.head_right_stun = pygame.image.load('Graphics/stun_dragon_head_right.png').convert_alpha()
			self.head_left_stun = pygame.image.load('Graphics/stun_dragon_head_left.png').convert_alpha()
			
			self.tail_up_stun = pygame.image.load('Graphics/dragon_tail_up.png').convert_alpha()
			self.tail_down_stun = pygame.image.load('Graphics/dragon_tail_down.png').convert_alpha()
			self.tail_right_stun = pygame.image.load('Graphics/dragon_tail_right.png').convert_alpha()
			self.tail_left_stun = pygame.image.load('Graphics/dragon_tail_left.png').convert_alpha()

			self.body_vertical_stun = pygame.image.load('Graphics/dragon_body_vertical.png').convert_alpha()
			self.body_horizontal_stun = pygame.image.load('Graphics/dragon_body_horizontal.png').convert_alpha()

			self.body_tr_stun = pygame.image.load('Graphics/dragon_body_tr.png').convert_alpha()
			self.body_tl_stun = pygame.image.load('Graphics/dragon_body_tl.png').convert_alpha()
			self.body_br_stun = pygame.image.load('Graphics/dragon_body_br.png').convert_alpha()
			self.body_bl_stun = pygame.image.load('Graphics/dragon_body_bl.png').convert_alpha()
	# stun hit
			self.head_up_stun_hit = pygame.image.load('Graphics/stun_dragon_head_up_hit.png').convert_alpha()
			self.head_down_stun_hit = pygame.image.load('Graphics/stun_dragon_head_down_hit.png').convert_alpha()
			self.head_right_stun_hit = pygame.image.load('Graphics/stun_dragon_head_right_hit.png').convert_alpha()
			self.head_left_stun_hit = pygame.image.load('Graphics/stun_dragon_head_left_hit.png').convert_alpha()
			
			self.tail_up_stun_hit = pygame.image.load('Graphics/dragon_tail_up_hit.png').convert_alpha()
			self.tail_down_stun_hit = pygame.image.load('Graphics/dragon_tail_down_hit.png').convert_alpha()
			self.tail_right_stun_hit = pygame.image.load('Graphics/dragon_tail_right_hit.png').convert_alpha()
			self.tail_left_stun_hit = pygame.image.load('Graphics/dragon_tail_left_hit.png').convert_alpha()

			self.body_vertical_stun_hit = pygame.image.load('Graphics/dragon_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_stun_hit = pygame.image.load('Graphics/dragon_body_horizontal_hit.png').convert_alpha()

			self.body_tr_stun_hit = pygame.image.load('Graphics/dragon_body_tr_hit.png').convert_alpha()
			self.body_tl_stun_hit = pygame.image.load('Graphics/dragon_body_tl_hit.png').convert_alpha()
			self.body_br_stun_hit = pygame.image.load('Graphics/dragon_body_br_hit.png').convert_alpha()
			self.body_bl_stun_hit = pygame.image.load('Graphics/dragon_body_bl_hit.png').convert_alpha()
		elif self.skin==2:
			self.head_up = pygame.image.load('Graphics/ant_head_up.png').convert_alpha()
			self.head_down = pygame.image.load('Graphics/ant_head_down.png').convert_alpha()
			self.head_right = pygame.image.load('Graphics/ant_head_right.png').convert_alpha()
			self.head_left = pygame.image.load('Graphics/ant_head_left.png').convert_alpha()
			
			self.tail_up = pygame.image.load('Graphics/ant_tail_up.png').convert_alpha()
			self.tail_down = pygame.image.load('Graphics/ant_tail_down.png').convert_alpha()
			self.tail_right = pygame.image.load('Graphics/ant_tail_right.png').convert_alpha()
			self.tail_left = pygame.image.load('Graphics/ant_tail_left.png').convert_alpha()

			self.body_vertical = pygame.image.load('Graphics/ant_body_vertical.png').convert_alpha()
			self.body_horizontal = pygame.image.load('Graphics/ant_body_horizontal.png').convert_alpha()

			self.body_tr = pygame.image.load('Graphics/ant_body_tr.png').convert_alpha()
			self.body_tl = pygame.image.load('Graphics/ant_body_tl.png').convert_alpha()
			self.body_br = pygame.image.load('Graphics/ant_body_br.png').convert_alpha()
			self.body_bl = pygame.image.load('Graphics/ant_body_bl.png').convert_alpha()
			self.crunch_sound = pygame.mixer.Sound('Sound/crunch.wav')
	# hit
			self.head_up_hit = pygame.image.load('Graphics/ant_head_up_hit.png').convert_alpha()
			self.head_down_hit = pygame.image.load('Graphics/ant_head_down_hit.png').convert_alpha()
			self.head_right_hit = pygame.image.load('Graphics/ant_head_right_hit.png').convert_alpha()
			self.head_left_hit = pygame.image.load('Graphics/ant_head_left_hit.png').convert_alpha()
			
			self.tail_up_hit = pygame.image.load('Graphics/ant_tail_up_hit.png').convert_alpha()
			self.tail_down_hit = pygame.image.load('Graphics/ant_tail_down_hit.png').convert_alpha()
			self.tail_right_hit = pygame.image.load('Graphics/ant_tail_right_hit.png').convert_alpha()
			self.tail_left_hit = pygame.image.load('Graphics/ant_tail_left_hit.png').convert_alpha()

			self.body_vertical_hit = pygame.image.load('Graphics/ant_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_hit = pygame.image.load('Graphics/ant_body_horizontal_hit.png').convert_alpha()

			self.body_tr_hit = pygame.image.load('Graphics/ant_body_tr_hit.png').convert_alpha()
			self.body_tl_hit = pygame.image.load('Graphics/ant_body_tl_hit.png').convert_alpha()
			self.body_br_hit = pygame.image.load('Graphics/ant_body_br_hit.png').convert_alpha()
			self.body_bl_hit = pygame.image.load('Graphics/ant_body_bl_hit.png').convert_alpha()
	# stun
			self.head_up_stun = pygame.image.load('Graphics/stun_ant_head_up.png').convert_alpha()
			self.head_down_stun = pygame.image.load('Graphics/stun_ant_head_down.png').convert_alpha()
			self.head_right_stun = pygame.image.load('Graphics/stun_ant_head_right.png').convert_alpha()
			self.head_left_stun = pygame.image.load('Graphics/stun_ant_head_left.png').convert_alpha()
			
			self.tail_up_stun = pygame.image.load('Graphics/ant_tail_up.png').convert_alpha()
			self.tail_down_stun = pygame.image.load('Graphics/ant_tail_down.png').convert_alpha()
			self.tail_right_stun = pygame.image.load('Graphics/ant_tail_right.png').convert_alpha()
			self.tail_left_stun = pygame.image.load('Graphics/ant_tail_left.png').convert_alpha()

			self.body_vertical_stun = pygame.image.load('Graphics/ant_body_vertical.png').convert_alpha()
			self.body_horizontal_stun = pygame.image.load('Graphics/ant_body_horizontal.png').convert_alpha()

			self.body_tr_stun = pygame.image.load('Graphics/ant_body_tr.png').convert_alpha()
			self.body_tl_stun = pygame.image.load('Graphics/ant_body_tl.png').convert_alpha()
			self.body_br_stun = pygame.image.load('Graphics/ant_body_br.png').convert_alpha()
			self.body_bl_stun = pygame.image.load('Graphics/ant_body_bl.png').convert_alpha()
	# stun hit
			self.head_up_stun_hit = pygame.image.load('Graphics/stun_ant_head_up_hit.png').convert_alpha()
			self.head_down_stun_hit = pygame.image.load('Graphics/stun_ant_head_down_hit.png').convert_alpha()
			self.head_right_stun_hit = pygame.image.load('Graphics/stun_ant_head_right_hit.png').convert_alpha()
			self.head_left_stun_hit = pygame.image.load('Graphics/stun_ant_head_left_hit.png').convert_alpha()
			
			self.tail_up_stun_hit = pygame.image.load('Graphics/ant_tail_up_hit.png').convert_alpha()
			self.tail_down_stun_hit = pygame.image.load('Graphics/ant_tail_down_hit.png').convert_alpha()
			self.tail_right_stun_hit = pygame.image.load('Graphics/ant_tail_right_hit.png').convert_alpha()
			self.tail_left_stun_hit = pygame.image.load('Graphics/ant_tail_left_hit.png').convert_alpha()

			self.body_vertical_stun_hit = pygame.image.load('Graphics/ant_body_vertical_hit.png').convert_alpha()
			self.body_horizontal_stun_hit = pygame.image.load('Graphics/ant_body_horizontal_hit.png').convert_alpha()

			self.body_tr_stun_hit = pygame.image.load('Graphics/ant_body_tr_hit.png').convert_alpha()
			self.body_tl_stun_hit = pygame.image.load('Graphics/ant_body_tl_hit.png').convert_alpha()
			self.body_br_stun_hit = pygame.image.load('Graphics/ant_body_br_hit.png').convert_alpha()
			self.body_bl_stun_hit = pygame.image.load('Graphics/ant_body_bl_hit.png').convert_alpha()
		self.head = self.head_left  # Vị trí ban đầu của đầu rắn 2
		self.tail = self.tail_right  # Vị trí ban đầu của đuôi rắn 2
	def draw_snake(self):
		self.update_head_graphics()
		self.update_tail_graphics()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
			
			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br,block_rect)

	def update_head_graphics(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left
		elif head_relation == Vector2(-1,0): self.head = self.head_right
		elif head_relation == Vector2(0,1): self.head = self.head_up
		elif head_relation == Vector2(0,-1): self.head = self.head_down

	def update_tail_graphics(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down

	def draw_snake_hit(self):
		self.update_head_graphics_hit()
		self.update_tail_graphics_hit()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical_hit,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal_hit,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl_hit,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br_hit,block_rect)

	def update_head_graphics_hit(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left_hit
		elif head_relation == Vector2(-1,0): self.head = self.head_right_hit
		elif head_relation == Vector2(0,1): self.head = self.head_up_hit
		elif head_relation == Vector2(0,-1): self.head = self.head_down_hit

	def update_tail_graphics_hit(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left_hit
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right_hit
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up_hit
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down_hit

	def draw_snake_stun(self):
		self.update_head_graphics_stun()
		self.update_tail_graphics_stun()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical_stun,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal_stun,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl_stun,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl_stun,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr_stun,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br_stun,block_rect)

	def update_head_graphics_stun(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left_stun
		elif head_relation == Vector2(-1,0): self.head = self.head_right_stun
		elif head_relation == Vector2(0,1): self.head = self.head_up_stun
		elif head_relation == Vector2(0,-1): self.head = self.head_down_stun

	def update_tail_graphics_stun(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left_stun
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right_stun
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up_stun
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down_stun

	def draw_snake_stun_hit(self):
		self.update_head_graphics_stun_hit()
		self.update_tail_graphics_stun_hit()

		for index,block in enumerate(self.body):
			x_pos = int(block.x * cell_size)
			y_pos = int(block.y * cell_size)
			block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

			if index == 0:
				screen.blit(self.head,block_rect)
			elif index == len(self.body) - 1:
				screen.blit(self.tail,block_rect)
			else:
				previous_block = self.body[index + 1] - block
				next_block = self.body[index - 1] - block
				if previous_block.x == next_block.x:
					screen.blit(self.body_vertical_stun_hit,block_rect)
				elif previous_block.y == next_block.y:
					screen.blit(self.body_horizontal_stun_hit,block_rect)
				else:
					if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
						screen.blit(self.body_tl_stun_hit,block_rect)
					elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
						screen.blit(self.body_bl_stun_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
						screen.blit(self.body_tr_stun_hit,block_rect)
					elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
						screen.blit(self.body_br_stun_hit,block_rect)

	def update_head_graphics_stun_hit(self):
		head_relation = self.body[1] - self.body[0]
		if head_relation == Vector2(1,0): self.head = self.head_left_stun_hit
		elif head_relation == Vector2(-1,0): self.head = self.head_right_stun_hit
		elif head_relation == Vector2(0,1): self.head = self.head_up_stun_hit
		elif head_relation == Vector2(0,-1): self.head = self.head_down_stun_hit

	def update_tail_graphics_stun_hit(self):
		tail_relation = self.body[-2] - self.body[-1]
		if tail_relation == Vector2(1,0): self.tail = self.tail_left_stun_hit
		elif tail_relation == Vector2(-1,0): self.tail = self.tail_right_stun_hit
		elif tail_relation == Vector2(0,1): self.tail = self.tail_up_stun_hit
		elif tail_relation == Vector2(0,-1): self.tail = self.tail_down_stun_hit

	def move_snake(self):
		if self.new_block == True:
			body_copy = self.body[:]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]
			self.new_block = False
		else:
			body_copy = self.body[:-1]
			body_copy.insert(0,body_copy[0] + self.direction)
			self.body = body_copy[:]

	def add_block(self):
		self.new_block = True

	def minus_snake(self):
		if self.minus_block == True:
			body_copy = self.body[:-2]
			self.body = body_copy[:]
			self.minus_block = False

	def play_crunch_sound(self):
		self.crunch_sound.play()

	def reset(self):
		self.body = [Vector2(cell_number-5, 10), Vector2(cell_number-6, 10), Vector2(cell_number-7, 10)]
		self.direction = Vector2(-1,0)
		self.save_direction = Vector2(-1,0)
  
	#Chỉ số tốc độ tăng lên khi đủ điểm
	def increase_speed(self):
		self.snake_speed += 2.5
		print("Snake speed : ",self.snake_speed)

	#Thiết lập thêm hàm speed cho chế độ
	def get_snake_speed(self):
		return self.snake_speed

class FRUIT:
    def __init__(self, blocked_positions):
        self.blocked_positions = blocked_positions
        self.randomize()
        self.random = False

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number * 8 // 13 - 1)
        self.pos = Vector2(self.x, self.y)

        # Kiểm tra nếu vị trí mới trùng với các vị trí đã bị chiếm (rắn, vật cản, quả táo khác)
        while self.pos in self.blocked_positions:
            self.x = random.randint(0, cell_number - 1)
            self.y = random.randint(0, cell_number * 8 // 13 - 1)
            self.pos = Vector2(self.x, self.y)

        # Sau khi tìm được vị trí hợp lệ, thêm nó vào danh sách các vị trí đã chiếm
        self.blocked_positions.append(self.pos)

# Fruit reverse
# mode là 1 thì mới chạy , thêm chức năng nếu mode là 2,3 thì sẽ chạy xuyên tường
class Reverse(FRUIT):
	def __init__(self,blocked_positions):
		self.randomize(blocked_positions)
		self.random = False
	def draw_fruit(self):
		fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
		screen.blit(mushroom,fruit_rect)
	def randomize(self, blocked_position):
		self.x = random.randint(0,cell_number-1)
		self.y = random.randint(0, cell_number*8//13 -1)
		self.pos = Vector2(self.x,self.y)
  
		while self.pos in blocked_position :
			self.x = random.randint(0,cell_number-1)
			self.y = random.randint(0, cell_number*8//13 -1)
			self.pos = Vector2(self.x,self.y)
   		# Sau khi tìm được vị trí hợp lệ, thêm nó vào danh sách các vị trí đã chiếm
		# self.blocked_positions.append(self.pos)

class BLOCK:
    def __init__(self, position=Vector2()):
        self.pos=position

    def draw_block(self):
        block_image = pygame.image.load('Graphics/block.png').convert_alpha()
        block_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(block_image, block_rect)

    def randomize(self, blocked_position):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0, cell_number*8//13 -1)
        self.pos = Vector2(self.x,self.y)
        while self.pos in blocked_position :
            self.x = random.randint(0,cell_number-1)
            self.y = random.randint(0, cell_number*8//13 -1)
            self.pos = Vector2(self.x,self.y)
            # Sau khi tìm được vị trí hợp lệ, thêm nó vào danh sách các vị trí đã chiếm
        # self.blocked_positions.append(self.pos)

class MAIN:
	def __init__(self,mode=0,skin=0):
		self.start=False
		self.snake = SNAKE(skin)
		self.snake2 = SNAKE2(skin)
		self.end = False
		self.is_paused = False
		self.blocked_positions=[]
		self.fruit = FRUIT(self.blocked_positions)
		self.fruit2 = FRUIT(self.blocked_positions)
		self.block = [] #khoi vat can
		if(mode !=0):
			self.mushroom = Reverse(self.blocked_positions)
		#SNAKE
		self.reverse_mushroom=False
		self.reverse_time=0
		self.score = 0
		self.save_score=0
		self.count_block=0
		self.create = False
		self.snake_increase = False
		#SNAKE2
		self.reverse_mushroom_snake2=False
		self.reverse_time_snake2 = 0
		self.score_snake2 = 0
		self.save_score_snake2 = 0
		self.count_block_snake2 = 0
		self.create2 = False
		self.snake2_increase = False
  
		self.mushroom_spawned = False
		self.modechosen=mode
		self.input_processed = False  # Cờ trạng thái cho bộ phím nhấn WASD
		self.input_processed2 = False  # Cờ trạng thái cho bộ phím nhấn mũi tên
		self.last_input_time = pygame.time.get_ticks()# Lưu thời gian (ms)
		self.last_input_time2 = pygame.time.get_ticks()

	def update(self):
		# self.input_processed = False  # Reset cờ trạng thái sau mỗi khung hình
		# self.input_processed2 = False
		if not self.create and len(self.block) < self.count_block:
			self.create = True
		if self.snake.hit_block == False:
			if self.snake.save_direction!= Vector2(0,0):
				self.snake.direction=self.snake.save_direction
				self.snake.save_direction=Vector2(0,0)
			self.snake.move_snake()
		else:
			if(self.snake.direction!=Vector2(0,0)):
				self.snake.save_direction=self.snake.direction
			self.snake.direction = Vector2(0,0)	
		if self.score >= 1:
			self.count_block=self.score
			if(self.count_block>4):
				# if(self.modechosen==0 or self.modechosen==1):
				self.count_block=4		
		else:
			self.count_block=0
		# Kiểm tra nếu cần tạo block mới
		if (not self.create or not self.create2) and len(self.block) < self.count_block:
			self.create = True

		# self.check_collision()

		if self.snake.minus_block ==True and self.snake.hit_block == True:
			self.snake.minus_snake()

		# self.check_fail()
		#SNAKE2
		if self.snake2.hit_block == False:
			if self.snake2.save_direction!= Vector2(-1,0):
				self.snake2.direction=self.snake2.save_direction
				self.snake2.save_direction=Vector2(-1,0)
			self.snake2.move_snake()
		else:
			if(self.snake2.direction!=Vector2(-1,0)):
				self.snake2.save_direction=self.snake2.direction
			self.snake2.direction = Vector2(-1,0)	
		if self.score>=5:
			self.count_block=self.score//5
			if(self.count_block>4):
				if(self.modechosen==0 or self.modechosen==1):
					self.count_block=4		
		else:
			self.count_block=0
		if self.create == True:
			# for i in range(len(self.block), self.count_block):
			self.create_new_block()
			self.create = False  # Đặt lại cờ

		self.check_collision()

		if self.snake2.minus_block ==True and self.snake2.hit_block == True:
			self.snake2.minus_snake()
			# self.score-=2	

		self.check_fail()
  
	def draw_elements(self):
		self.draw_grass()
		self.fruit.draw_fruit()
		self.fruit2.draw_fruit()
		if(self.modechosen !=0):
			self.mushroom.draw_fruit()
		#SNAKE1
		if self.snake.hit_block == True and self.reverse_mushroom==False:
			if self.snake.second_flash <50 or self.snake.second_flash>100 and self.snake.second_flash<150:
				self.snake.draw_snake()
			elif  self.snake.second_flash >50 and self.snake.second_flash<101 or self.snake.second_flash>150:
				self.snake.draw_snake_hit()
			self.snake.second_flash +=1
		elif self.snake.hit_block == False and self.reverse_mushroom==False:
			self.snake.draw_snake()
		elif self.snake.hit_block == False and self.reverse_mushroom==True:
			self.snake.draw_snake_stun()
		elif self.snake.hit_block == True and self.reverse_mushroom==True:
			if self.snake.second_flash <50 or self.snake.second_flash>100 and self.snake.second_flash<150:
				self.snake.draw_snake()
			elif  self.snake.second_flash >50 and self.snake.second_flash<101 or self.snake.second_flash>150:
				self.snake.draw_snake_stun_hit()	
			self.snake.second_flash +=1		
		if self.snake.second_flash == 200:
			self.snake.second_flash =0
			self.snake.hit_block = False
		#SNAKE2
		if self.snake2.hit_block == True and self.reverse_mushroom_snake2==False:
			if self.snake2.second_flash <50 or self.snake2.second_flash>100 and self.snake2.second_flash<150:
				self.snake2.draw_snake()
			elif  self.snake2.second_flash >50 and self.snake2.second_flash<101 or self.snake2.second_flash>150:
				self.snake2.draw_snake_hit()
			self.snake2.second_flash +=1
		elif self.snake2.hit_block == False and self.reverse_mushroom_snake2==False:
			self.snake2.draw_snake()
		elif self.snake2.hit_block == False and self.reverse_mushroom_snake2==True:
			self.snake2.draw_snake_stun()
		elif self.snake2.hit_block == True and self.reverse_mushroom_snake2==True:
			if self.snake2.second_flash <50 or self.snake2.second_flash>100 and self.snake2.second_flash<150:
				self.snake2.draw_snake()
			elif  self.snake2.second_flash >50 and self.snake2.second_flash<101 or self.snake2.second_flash>150:
				self.snake2.draw_snake_stun_hit()	
			self.snake2.second_flash +=1		
		if self.snake2.second_flash == 200:
			self.snake2.second_flash =0
			self.snake2.hit_block = False
   
		if len(self.block)>0:
			for i in range(0,len(self.block)):
				pos_block=self.block[i]
				block=BLOCK(pos_block)
				block.draw_block()
		# else : 
		# 	block = BLOCK(Vector2(5, 5))  # Vẽ thử một khối cố định
		# 	block.draw_block()
		# 	self.block.append(block)
		self.draw_score()

	def check_collision(self):
# fruit
		#SNAKE1
		if self.fruit.pos == self.snake.body[0]:
			self.fruit.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()

			self.score += 1
			self.create = True
   
			if self.score % 5 ==0:
				if not self.snake_increased:
					self.snake.increase_speed()
					self.snake_increased = True

			self.blocked_positions.clear()
			self.block.clear()
			pos_fruit=Vector2(self.fruit.x,self.fruit.y)
			pos_snake=Vector2(self.snake.body[0].x,self.snake.body[0].y)
			pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
			for i in range(0,6):
				pos_temp=pos_distance[i]+pos_snake
				self.blocked_positions.append(pos_temp)
			self.blocked_positions.append(pos_fruit)
			
		elif self.fruit2.pos == self.snake.body[0]:
			self.fruit2.randomize()
			self.snake.add_block()
			self.snake.play_crunch_sound()

			self.score += 1
			self.create = True
   
			if self.score % 5 ==0:
				if not self.snake_increased:
					self.snake.increase_speed()
					self.snake_increased = True

			self.blocked_positions.clear()
			self.block.clear()
			pos_fruit2=Vector2(self.fruit2.x,self.fruit2.y)
			pos_snake=Vector2(self.snake.body[0].x,self.snake.body[0].y)
			pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
			for i in range(0,6):
				pos_temp=pos_distance[i]+pos_snake
				self.blocked_positions.append(pos_temp)
			self.blocked_positions.append(pos_fruit2)
			
		else:
			self.snake_increased = False
		#SNAKE2
		if self.fruit.pos == self.snake2.body[0]:
			self.fruit.randomize()
			self.snake2.add_block()
			self.snake2.play_crunch_sound()

			self.score += 1
			self.create2 = True
   
			if self.score % 5 ==0:
				if not self.snake2_increased:
					self.snake2.increase_speed()
					self.snake2_increased = True

			self.blocked_positions.clear()
			self.block.clear()
			pos_fruit=Vector2(self.fruit.x,self.fruit.y)
			pos_snake2=Vector2(self.snake2.body[0].x,self.snake2.body[0].y)
			pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
			for i in range(0,6):
				pos_temp=pos_distance[i]+pos_snake2
				self.blocked_positions.append(pos_temp)
			self.blocked_positions.append(pos_fruit)

		elif self.fruit2.pos == self.snake2.body[0]:
			self.fruit2.randomize()
			self.snake2.add_block()
			self.snake2.play_crunch_sound()

			self.score += 1
			self.create2 = True
   
			if self.score % 5 ==0:
				if not self.snake2_increased:
					self.snake2.increase_speed()
					self.snake2_increased = True

			self.blocked_positions.clear()
			self.block.clear()
			pos_fruit2=Vector2(self.fruit2.x,self.fruit2.y)
			pos_snake2=Vector2(self.snake2.body[0].x,self.snake2.body[0].y)
			pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
			for i in range(0,6):
				pos_temp=pos_distance[i]+pos_snake2
				self.blocked_positions.append(pos_temp)
			self.blocked_positions.append(pos_fruit2)
			
		else:
			self.snake2_increased = False
		if self.modechosen!=0:
			if not self.mushroom_spawned:  # Chỉ spawn nếu Mushroom chưa tồn tại
				self.mushroom.randomize(self.blocked_positions)
				pos_mushroom = Vector2(self.mushroom.x, self.mushroom.y)
				self.blocked_positions.append(pos_mushroom)
				self.mushroom_spawned = True  # Đánh dấu Mushroom đã spawn
# Mushroom
		if(self.modechosen!=0):
			if self.mushroom.pos == self.snake.body[0]:	
				self.reverse_mushroom=True
				self.reverse_time=0
				self.mushroom_spawned = False  # Đặt lại để cho phép spawn Mushroom mới
				self.mushroom.randomize(self.blocked_positions)
			if self.mushroom.pos == self.snake2.body[0]:	
				self.reverse_mushroom_snake2=True
				self.reverse_time_snake2=0
				self.mushroom_spawned = False  # Đặt lại để cho phép spawn Mushroom mới
				self.mushroom.randomize(self.blocked_positions)
# block
		for i in range(0,len(self.block)):
			if self.block[i] == self.snake.body[0]:
				self.fruit.randomize()
				self.fruit2.randomize()
				self.blocked_positions.clear()
				self.block.clear()
				pos_fruit=Vector2(self.fruit.x,self.fruit.y)
				pos_fruit2=Vector2(self.fruit2.x,self.fruit2.y)
				pos_snake=Vector2(self.snake.body[0].x,self.snake.body[0].y)
				pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
				for i in range(0,6):
					pos_temp=pos_distance[i]+pos_snake
					self.blocked_positions.append(pos_temp)
				self.blocked_positions.append(pos_fruit)
				self.blocked_positions.append(pos_fruit2)
				if self.modechosen!=0:
					self.mushroom.randomize(self.blocked_positions)
					pos_mushroom=Vector2(self.mushroom.x,self.mushroom.y)
					self.blocked_positions.append(pos_mushroom)		

				self.create = True

				self.snake.hit_block = True
				self.snake.minus_block = True
				self.snake.second_flash =0
			elif self.block[i] == self.snake2.body[0]:
				self.fruit.randomize()
				self.fruit2.randomize()
				self.blocked_positions.clear()
				self.block.clear()
				pos_fruit=Vector2(self.fruit.x,self.fruit.y)
				pos_fruit2=Vector2(self.fruit2.x,self.fruit2.y)
				pos_snake2=Vector2(self.snake2.body[0].x,self.snake2.body[0].y)
				pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
				for i in range(0,6):
					pos_temp=pos_distance[i]+pos_snake2
					self.blocked_positions.append(pos_temp)
				self.blocked_positions.append(pos_fruit)
				self.blocked_positions.append(pos_fruit2)
				if self.modechosen!=0:
					self.mushroom.randomize(self.blocked_positions)
					pos_mushroom=Vector2(self.mushroom.x,self.mushroom.y)
					self.blocked_positions.append(pos_mushroom)		

				self.create2 = True

				self.snake2.hit_block = True
				self.snake2.minus_block = True
				self.snake2.second_flash =0
				break
# spawn fruit,block
		for block in self.snake.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()
			if block == self.fruit2.pos:
				self.fruit2.randomize()
			if self.modechosen!=0:
				if block ==self.mushroom.pos:
					self.mushroom.randomize(self.blocked_positions)
			for i in range(0,len(self.block)):
				if block ==self.block[i]:
					self.blocked_positions.clear()
					self.block.clear()
					pos_fruit=Vector2(self.fruit.x,self.fruit.y)
					pos_fruit2=Vector2(self.fruit2.x,self.fruit2.y)
					pos_snake=Vector2(self.snake.body[0].x,self.snake.body[0].y)
					pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
					for i in range(0,6):
						pos_temp=pos_distance[i]+pos_snake
						self.blocked_positions.append(pos_temp)
					self.blocked_positions.append(pos_fruit)
					self.blocked_positions.append(pos_fruit2)
					if self.modechosen!=0:
						pos_mushroom=Vector2(self.mushroom.x,self.mushroom.y)
						self.blocked_positions.append(pos_mushroom)	
					self.create = True
					break
		for block in self.snake2.body[1:]:
			if block == self.fruit.pos:
				self.fruit.randomize()
			if block == self.fruit2.pos:
				self.fruit2.randomize()
			if self.modechosen!=0:
				if block ==self.mushroom.pos:
					self.mushroom.randomize(self.blocked_positions)
			for i in range(0,len(self.block)):
				if block ==self.block[i]:
					self.blocked_positions.clear()
					self.block.clear()
					pos_fruit=Vector2(self.fruit.x,self.fruit.y)
					pos_fruit2=Vector2(self.fruit2.x,self.fruit2.y)
					pos_snake2=Vector2(self.snake2.body[0].x,self.snake2.body[0].y)
					pos_distance=[Vector2(2,0),Vector2(2,2),Vector2(0,2),Vector2(1,0),Vector2(1,1),Vector2(0,1),]
					for i in range(0,6):
						pos_temp=pos_distance[i]+pos_snake2
						self.blocked_positions.append(pos_temp)
					self.blocked_positions.append(pos_fruit)
					self.blocked_positions.append(pos_fruit2)
					if self.modechosen!=0:
						pos_mushroom=Vector2(self.mushroom.x,self.mushroom.y)
						self.blocked_positions.append(pos_mushroom)	
					self.create = True
					break


	def create_new_block(self):
		block_x=random.randint(0,cell_number-1)
		block_y=random.randint(0,cell_number*8//13-1)	
		block_pos=Vector2(block_x,block_y)
		while block_pos  in self.blocked_positions:
			block_x=random.randint(0,cell_number-1)
			block_y=random.randint(0,cell_number*8//13-1)	
			block_pos=Vector2(block_x,block_y)				
		self.blocked_positions.append(block_pos)
		self.block.append(block_pos)		
		print(f"New block created at {block_pos}")


	
	def check_fail(self):
		# Kiểm tra va chạm của Snake1 với chính nó
		if self.start and not self.is_paused:  # Chỉ kiểm tra nếu trò chơi đã bắt đầu
			if len(self.snake.body) > 4:
				if self.snake.body[0] in self.snake.body[1:]:
					print("Snake1 collided with itself!")
					self.score_snake2 = 0
					self.end = True
			# Kiểm tra va chạm của Snake2 với chính nó
			if len(self.snake2.body) > 4:
				if self.snake2.body[0] in self.snake2.body[1:]:
					print("Snake2 collided with itself!")
					self.score_snake2 = 1
					self.end = True
			
			if self.snake.body[0] in self.snake2.body:
			# Kiểm tra va chạm giữa Snake2 và Snake1
				if self.snake2.body[0] in self.snake.body:
					print("No one win")
					self.score_snake2 = 3
					self.end = True  # Kết thúc trò chơi
			# Kiểm tra va chạm giữa Snake1 và Snake2
			if self.snake.body[0] in self.snake2.body[1:]:
				print("Snake1 collided with Snake2!")
				self.score_snake2 = 0
				self.end = True  # Kết thúc trò chơi
			# Kiểm tra va chạm giữa Snake2 và Snake1
			elif self.snake2.body[0] in self.snake.body[1:]:
				print("Snake2 collided with Snake1!")
				self.score_snake2 = 1
				self.end = True  # Kết thúc trò chơi

		if self.snake.hit_block==True:
			print('Snake 1 chet do tong vao vat can')
			self.snake.hit_block = False
			self.snake.minus_block = False
			self.reverse_mushroom=False
			self.reverse_time=0
			self.snake.second_flash =0
			self.snake.save_direction=Vector2(0,0)
			self.fruit.random=True
			self.score_snake2 = 0
			self.score_board()
			self.game_over()
		if self.snake2.hit_block==True:
			print('Snake 2 chet do tong vao vat can')
			self.snake2.hit_block = False
			self.snake2.minus_block = False
			self.reverse_mushroom_snake2=False
			self.reverse_time_snake2=0
			self.snake2.second_flash =0
			self.snake2.save_direction=Vector2(-1,0)
			self.fruit.random=True
			self.score_snake2 = 1
			self.score_board()
			self.game_over()

		if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number*8//13:
			if self.modechosen==1 or  self.modechosen==0:
				print('Snake 1 chet do tong vao tuong')
				self.fruit.random=True
				self.fruit2.random=True
				self.score_snake2 = 0
				self.score_board()
				self.game_over()
				# or  self.modechosen==0
				# print('di xuyen vao tuong')
				# lưu ý duyệt qua từng bộ phận chứ không phải toàn bộ
				# nếu self.snake.body đi qua thì x==0 thì vector sẽ bằng(cell_number,y) và ngược lại
				# nếu self.snake.body đi qua thì x==0 thì vector sẽ bằng(x,cell_number*8//13) và ngược lại
				# chạy bên ngoài if này và xét nếu modechosen!=0,1 
				# làm ở hàm update 
		if not 0 <= self.snake2.body[0].x < cell_number or not 0 <= self.snake2.body[0].y < cell_number*8//13:
			if self.modechosen==1 or  self.modechosen==0:
				print('Snake 2 chet do tong vao tuong')
				self.fruit.random=True
				self.fruit2.random=True
				self.score_snake2 = 1
				self.score_board()
				self.game_over()
		direction=self.snake.direction
		for i in range(len(self.snake.body)):
			block=self.snake.body[i]
			if(direction==Vector2(-1,0) and block.x<0):
				block.x=cell_number-1
				self.check_collision()
			elif(direction==Vector2(1,0) and block.x>=cell_number):
				block.x=0
				self.check_collision()
			elif(direction==Vector2(0,-1) and block.y<0):
				block.y=cell_number*8//13-1
				self.check_collision()
			elif(direction==Vector2(0,1) and block.y>=cell_number*8//13):
				block.y=0
				self.check_collision()
		direction2=self.snake2.direction
		for i in range(len(self.snake2.body)):
			block=self.snake2.body[i]
			if(direction2==Vector2(-1,0) and block.x<0):
				block.x=cell_number-1
				self.check_collision()
			elif(direction2==Vector2(1,0) and block.x>=cell_number):
				block.x=0
				self.check_collision()
			elif(direction2==Vector2(0,-1) and block.y<0):
				block.y=cell_number*8//13-1
				self.check_collision()
			elif(direction2==Vector2(0,1) and block.y>=cell_number*8//13):
				block.y=0
				self.check_collision()	
		for block in self.snake.body[1:]:
			if block == self.snake.body[0] and self.start==False:
				self.game_over()
			elif block==self.snake.body[0] and self.start==True:
				self.score_board()
				self.game_over()
		for block in self.snake2.body[1:]:
			if block == self.snake2.body[0] and self.start==False:
				self.game_over()
			elif block==self.snake2.body[0] and self.start==True:
				self.score_board()
				self.game_over()
		
	def game_over(self):
		self.reset()
	def reset(self):
		self.start=False
		if(self.fruit.random==True):
			self.fruit.randomize()
			self.fruit.random=False
		if(self.fruit2.random==True):
			self.fruit2.randomize()
			self.fruit2.random=False
		self.is_paused = False  # Thoát khỏi màn hình pause
		self.blocked_positions.clear()
		self.block.clear()
		self.score = 0
		self.reverse_mushroom=False
		self.reverse_time_snake=0	
		self.reverse_mushroom_snake2=False
		self.reverse_time_snake2=0			
		self.count_block=0
		self.snake.reset()
		self.snake2.reset()
	def score_board(self):
		self.save_score=self.score
		self.end=True
	def draw_grass(self):
		grass_color = (167,209,61)
		for row in range(cell_number):
			if row % 2 == 0: 
				for col in range(cell_number):
					if col % 2 == 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)
			else:
				for col in range(cell_number):
					if col % 2 != 0:
						grass_rect = pygame.Rect(col * cell_size,row * cell_size,cell_size,cell_size)
						pygame.draw.rect(screen,grass_color,grass_rect)			

	def draw_score(self):
		score_text = str(len(self.snake.body) + len(self.snake2.body) - 3 - 3)
		score_surface = game_font.render("Score: " + score_text, True, (56, 74, 12))

		# Đặt độ trong suốt cho chữ "Score"
		score_surface.set_alpha(100)

		score_rect = score_surface.get_rect(topright=(SCREEN_WIDTH - 10, 40))

		# Vẽ chữ "Score" lên màn hình
		screen.blit(score_surface, score_rect)
		bg_rect = pygame.Rect(score_rect.left - 6, score_rect.top, score_rect.width + 6, score_rect.height)

		pygame.draw.rect(screen, (167, 209, 61), bg_rect)
		screen.blit(score_surface, score_rect)
		pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
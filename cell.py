import pygame

class Cell:
	def __init__(self, x, y, color, win):
		self.x = x
		self.y = y
		self.color = color
		self.win = win
	def draw(self):
		pygame.draw.rect(self.win, self.color, (self.x * 10, self.y * 10, 10, 10))
	def change_color(self, color):
		self.color = color
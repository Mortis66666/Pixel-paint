import json
import os
import pygame

from cell import Cell

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH = win.get_width()
HEIGHT = win.get_height()


# Colors
WHITE = "white"
BLACK = "black"

# Grid
grid = [[]]
with open("edit.txt", "r") as file:
	edit = file.read()
	if edit.isdigit():
		with open(f"datas/data{edit}.json", "r") as data_file:
			datas = json.load(data_file)
			grid = [[Cell(x, y, color, win) for x, y, color in row] for row in datas]
	else:
		grid = [[Cell(x, y, WHITE, win) for x in range(WIDTH//10)] for y in range(HEIGHT//10)]


colors = [
	"white",
	"red",
	"orange",
	"yellow",
	"green",
	"blue",
	"indigo",
	"purple",
	"#964B00",
	"black"
]

def draw_line():
	for x in range(0, WIDTH, 10): # Draw vertical lines
		pygame.draw.line(win, BLACK, (x, 0), (x, HEIGHT - 1))
	for y in range(0, HEIGHT, 10): # Draw horizontal lines
		pygame.draw.line(win, BLACK, (0, y), (WIDTH-1, y))

def draw_color(color):
	pygame.draw.circle(win, color, (40, HEIGHT - 40), 30)

def draw(color):
	win.fill((255, 255, 255))

	for row in grid:
		for cell in row:
			cell.draw()

	draw_line()
	draw_color(color)
	pygame.display.update()

def handle_click(color):
	x, y = pygame.mouse.get_pos()
	x, y = x//10, y//10

	grid[y][x].change_color(color)

def get_id(folder):
	try:
		return int(os.listdir(folder)[-1][3:-4]) + 1
	except:
		return 1

def save():
	pygame.image.save(win, f"images/pic{get_id('images')}.jpg")

	with open(f"datas/data{get_id('data')}.json", "w") as f:
		json.dump([[[cell.x, cell.y, cell.color] for cell in row] for row in grid], f)

def main():
	FPS = 60
	clock = pygame.time.Clock()
	run = True
	index = 0

	while run:
		clock.tick(FPS)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return
			elif event.type == pygame.KEYDOWN:
				pressed = pygame.key.get_pressed()
				if pressed[pygame.K_q] or pressed[pygame.K_ESCAPE] or pressed[pygame.K_F11]:
					run = False
					return
				if pressed[pygame.K_LEFT]:
					index = (len(colors) + index - 1) % len(colors)
				if pressed[pygame.K_RIGHT]:
					index = (len(colors) + index + 1) % len(colors)
				if (pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]) and pressed[pygame.K_s]:
					save()

			elif event.type == pygame.MOUSEBUTTONDOWN:
				handle_click(colors[index])

		draw(colors[index])


if __name__ == "__main__":
	main()
	pygame.quit()
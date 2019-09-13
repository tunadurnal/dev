import pygame, random

width = 360
height = 480
fps = 30

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Yarrak')
clock = pygame.time.Clock()

# Game loop
running = True
while running:
	clock.tick(fps)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill(green)
	pygame.display.flip()

pygame.quit()
import pygame
from random import randrange

pygame.init()
white = (255,255,255)
black = (0,0,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Random Shooter')
clock = pygame.time.Clock()
tank = pygame.image.load('tank.png')
ates = pygame.mixer.Sound('ates.wav')

def game():
    FPS = 70
    tank_x = display_width / 2 - 200 / 2
    tank_y = display_height * 0.85
    tank_x_change = 0
    tank_y_change = 0
    num = 0
    basla = 0
    ball_size = 10
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound.play(ates)
                    basla = 1
                    exec('ball_x' + str(num) + ' = ' + str(tank_x + 100 - ball_size / 2))
                    exec('ball_y' + str(num) + ' = ' + str(tank_y))
                    num += 1
                if event.key == pygame.K_LEFT:
                    tank_x_change = -5
                if event.key == pygame.K_RIGHT:
                    tank_x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank_x_change = 0
        gameDisplay.fill(black)
        tank_x += tank_x_change
        gameDisplay.blit(tank, (tank_x, tank_y))
        if basla == 1:
            i = 0
            while i < num:
                if not eval('ball_y' + str(i)) <= 0:
                    pygame.draw.rect(gameDisplay, white, (eval('ball_x' + str(i)), eval('ball_y' + str(i)), ball_size, ball_size))
                    exec('ball_y' + str(i) + ' -= 5')
                i += 1
        if tank_x <= 5:
            tank_x = 10
        elif tank_x + 200 >= 795:
            tank_x = 590
        pygame.display.update()
        clock.tick(FPS)

game()

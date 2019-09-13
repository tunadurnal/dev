import pygame
from random import randrange

pygame.init()
white = (255,255,255)
black = (0,0,0)
light_red = (255,0,0)
red = (155,0,0)
green = (0,100,0)
original_green = (0,155,0)
light_green = (0,255,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Yılan')
clock = pygame.time.Clock()
kaybettin = pygame.font.SysFont('comicsansms', 100)
small_font = pygame.font.SysFont('comicsansms', 15)

def text_objects(text, color, font):
    textSurf = eval(font).render(text, True, color)
    return textSurf, textSurf.get_rect()

def mesage_to_screen(text, color, font, x_change=0, y_change=0, special=False):
    textSurf, textRect = text_objects(text, color, font)
    if special:
        textRect.center = ((x_change), (y_change))
    else:
        textRect.center = ((display_width / 2) + x_change, (display_height / 2) + y_change)
    gameDisplay.blit(textSurf, textRect)

def create_apple(AppleSize):
    RandomAppleX = round(randrange(0, display_width - AppleSize)/10)*10
    RandomAppleY = round(randrange(0, display_height - AppleSize)/10)*10
    return RandomAppleX, RandomAppleY

def button(x, y, width, height, color, light_color, text, action1=None, action2=None, repeat=1):
        mousePos = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        if x < mousePos[0] < x+width and y < mousePos[1] < y+height:
            pygame.draw.rect(gameDisplay, light_color, (x, y, width, height))
            if pressed[0] == 1:
                if repeat == 1:
                    eval(action1)
                elif repeat == 2:
                    eval(action1)
                    eval(action2)
                else:
                    print('repeat değişkeni geçersiz bir değer içermekte.')
        else:
            pygame.draw.rect(gameDisplay, color, (x, y, width, height))
        mesage_to_screen(text, black, 'small_font', x+width/2, y+height/2, True)
        pygame.display.update()

def snake(snakeList, size, direction, head):
    for i in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, original_green, (i[0], i[1], size, size))
    if direction == 'down':
        head = pygame.transform.rotate(head, 180)
    if direction == 'left':
        head = pygame.transform.rotate(head, 90)
    if direction == 'right':
        head = pygame.transform.rotate(head, 270)
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))
    
def game():
    head = pygame.image.load('snakeHead.png')
    direction = 'up'
    FPS = 50
    size = 20
    lead_x = display_width / 2 - size
    lead_y = display_height / 2 - size
    lead_x_change = 0
    lead_y_change = 0
    gameExit = False
    gameOver = False
    AppleSize = 30
    RandomAppleX, RandomAppleY = create_apple(AppleSize)
    snakeLenght = 1
    snakeList = []
    while not gameExit:
        while gameOver == True:
            mesage_to_screen('Kaybettin', light_red, 'kaybettin', y_change=-100)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                button(200, 400, 100, 50, green, light_green, 'Yeniden Oyna', 'game()')
                button(500, 400, 100, 50, red, light_red, 'Çıkış', 'pygame.quit()', 'quit()', 2)
                pygame.display.update()
                clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    direction = 'up'
                    lead_y_change = -10
                    lead_x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    direction = 'down'
                    lead_y_change = 10
                    lead_x_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    direction = 'left'
                    lead_y_change = 0
                    lead_x_change = -10
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    direction = 'right'
                    lead_y_change = 0
                    lead_x_change = 10

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, light_red, (RandomAppleX, RandomAppleY, AppleSize, AppleSize))
        # Kenarlara carpti mi kontrol et
        if lead_x >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y <= 0:
            gameOver = True
        # Elmayi yedi mi kontrol et
        if lead_x > RandomAppleX and lead_x < RandomAppleX + AppleSize or lead_x+size > RandomAppleX and lead_x+size < RandomAppleX + AppleSize:
            if lead_y > RandomAppleY and lead_y < RandomAppleY + AppleSize or lead_y+size > RandomAppleY and lead_y+size < RandomAppleY + AppleSize:
                RandomAppleX, RandomAppleY = create_apple(AppleSize)
                snakeLenght += 1
                FPS += 1
        snakeHead = [lead_x, lead_y]
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLenght:
            del snakeList[0]
        for i in snakeList[:-1]:
            if i == snakeHead:
                gameOver = True
        snake(snakeList, size, direction, head)
        pygame.display.update()
        clock.tick(FPS)
game()

































        

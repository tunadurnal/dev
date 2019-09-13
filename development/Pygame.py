import pygame

pygame.init()
white = (255,255,255)
black = (0,0,0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('DVD')
clock = pygame.time.Clock()
font = pygame.font.SysFont('comicsansms', 20)
sony = pygame.image.load('sony.png')

def mesage_to_screen(msg, color):
    text = font.render(msg, True, color)
    gameDisplay.blit(text, (5, 3))

def game():
    FPS = 70
    x_size = 75
    y_size = 38
    lead_x = display_width / 2 - (x_size / 2)
    lead_y = display_height / 2 - (y_size / 2)
    lead_x_change = 0
    lead_y_change = 0
    basladi = False
    isi_bitir  = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not basladi:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        basladi = True

        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        if not basladi:
            mesage_to_screen('Başlatmak için SPACE\'e basın', black)
        else:
            if not isi_bitir:
                lead_x_change = 10
                lead_y_change = -10
                isi_bitir = True
        gameDisplay.blit(sony, (lead_x, lead_y))
        if lead_x <= 0:
            lead_x_change = 10
        if lead_x + x_size >= display_width:
            lead_x_change = -10
        if lead_y <= 0:
            lead_y_change = 10
        if lead_y + y_size >= display_height:
            lead_y_change = -10
        pygame.display.update()
        clock.tick(FPS)
game()
















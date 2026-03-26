import sys, pygame

pygame.init()
pygame.font.init()
#text_font = pygame.font.SysFont('Comic Sans MS', 58)

#Bildschirmposition festlegen

#text_surface = text_font.render('text', False, (225, 225, 225))

#-------SCREEN--------------------------------------------------
screen_width = 1360
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255, 255, 255))

#............ TASTEN .................................................

#-------LEAVE MEETING TASTE------------------------------------
button_width = 200
button_height = 50
button_image = pygame.image.load("Leave Meeting Taste.png")
button_image = pygame.transform.scale(button_image, (button_width, button_height))
button_position = (screen_width - button_width, screen_height - button_height)
button_rect = button_image.get_rect()
button_rect.topleft = button_position
#--------------------------------------------------------------
#......................................................................

clock = pygame.time.Clock()

game_on = True
while game_on:
    clock.tick(60)
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                game_on = False
               
    screen.blit(button_image, (button_position))
    pygame.display.flip()
    
sys.exit()



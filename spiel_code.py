import sys, pygame

pygame.init()
pygame.font.init()
#text_font = pygame.font.SysFont('Comic Sans MS', 58)

#Bildschirmposition festlegen

#text_surface = text_font.render('text', False, (225, 225, 225))

position = 460, 300
size = 400, 200
button_rect = pygame.Rect(position, size)


#SCREEN :
screen_width = 1360
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((189, 214, 240))

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
               
    pygame.draw.rect(screen, (0, 9, 9), button_rect)
    #pygame.draw.rect(screen, (214, 114, 212), rect)
    #screen.blit(button, button_position)
    #screen.blit(text_surface, (25,200))
                    
    pygame.display.flip()
    #pygame.display.update()
    
sys.exit()



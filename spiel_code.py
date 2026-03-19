import sys, pygame

pygame.init()
pygame.font.init()
#text_font = pygame.font.SysFont('Comic Sans MS', 58)

#Bildschirmposition festlegen

#text_surface = text_font.render('text', False, (225, 225, 225))

position = 50, 50
size = 50, 50
button_rect = pygame.Rect(position, size)


#SCREEN :
screen_width = 1360
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))



clock = pygame.time.Clock()

while 1:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                game_on = True
               
    screen.fill((176, 111, 171))
   
    pygame.draw.rect(screen, (0, 9, 9), button_rect)
    #pygame.draw.rect(screen, (214, 114, 212), rect)
    #screen.blit(button, button_position)
    #screen.blit(text_surface, (25,200))
                    
    pygame.display.flip()
    #pygame.display.update()


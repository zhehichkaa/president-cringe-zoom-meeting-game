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

#................... TASTEN .................................................

#-------LEAVE MEETING TASTE------------------------------------
button_width = 200
button_height = 50
button_image = pygame.image.load("Leave Meeting Taste.png")
button_image = pygame.transform.scale(button_image, (button_width, button_height))
button_position = (screen_width - button_width, screen_height - button_height)
button_rect = button_image.get_rect()
button_rect.topleft = button_position
#--------------------------------------------------------------

#-------CHAT------------------------------------------
Chat_width = 150
Chat_height = 50
Chat_image = pygame.image.load("Chat.png")
Chat_image = pygame.transform.scale(Chat_image, (Chat_width, Chat_height))
Chat_position = (450, 750)    #(screen_width - Chat_width, screen_height - Chat_height)
Chat_rect = Chat_image.get_rect()
Chat_rect.topleft = Chat_position

chatpanel_width = 500
chatpanel_height = 700
chatpanel = pygame.image.load("chatpanel.png")
chatpanel = pygame.transform.scale(chatpanel, (chatpanel_width, chatpanel_height))
chatpanel_position = (200, 70)
#--------------------------------------------------------------
#......................................................................

clock = pygame.time.Clock()

show_chat_panel = False

game_on = True
while game_on:
    clock.tick(60)
    for event in pygame.event.get():
        #print(event.type)
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                game_on = False
            if Chat_rect.collidepoint(event.pos):
                print (show_chat_panel)
                show_chat_panel = not show_chat_panel
                
#.............. TASTEN EINZEIGEN .......................
    screen.fill((0, 0, 0))
                
    if (show_chat_panel):
        screen.blit(chatpanel, (chatpanel_position))
    screen.blit(Chat_image, (Chat_position))
    screen.blit(button_image, (button_position))
    
    pygame.display.flip()
    
sys.exit()



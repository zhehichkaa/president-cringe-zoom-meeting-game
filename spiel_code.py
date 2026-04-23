import sys, pygame

pygame.init()
pygame.font.init()
#text_font = pygame.font.SysFont('Comic Sans MS', 58)

#Bildschirmposition festlegen

#text_surface = text_font.render('text', False, (225, 225, 225))

#----------------------------classen---------------------------------------
class Button:
    def __init__(self, filename, width, height, x, y):
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.topleft))
        
#-------SCREEN--------------------------------------------------
screen_width = 1360
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#................... TASTEN .................................................
leave_button = Button("Leave Meeting Taste.png", 200, 50, screen_width - 200, screen_height - 50)
chat_button =  Button("Chat.png", 150, 50, 450, 750) 

chatpanel_width = 500
chatpanel_height = 700
chatpanel = pygame.image.load("chatpanel.png")
chatpanel = pygame.transform.scale(chatpanel, (chatpanel_width, chatpanel_height))
chatpanel_position = (200, 70)
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
            if leave_button.rect.collidepoint(event.pos):
                game_on = False
            if chat_button.rect.collidepoint(event.pos):
                show_chat_panel = not show_chat_panel
                
#.............. TASTEN EINZEIGEN .......................
    screen.fill((0, 0, 0))
                
    if (show_chat_panel):
        screen.blit(chatpanel, (chatpanel_position))
    chat_button.draw(screen)
    leave_button.draw(screen)
    
    pygame.display.flip()
    
sys.exit()



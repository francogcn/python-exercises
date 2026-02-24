import pygame
pygame.init()
WHITE = (255,255,255)
BLACK=(0,0,0)
size = WIDTH,HEIGHT = (800,500)
screen = pygame.display.set_mode(size)
run = True

def colorear(color):
    screen.fill(color)
    pygame.display.update()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #Controles con flechas
        if event.type == pygame.KEYDOWN:
            if event.key == 1073741906: #Flecha arriba
                colorear(WHITE)
                
            if event.key == 1073741905: #flecha abajo
                colorear((10,200,150))
            
            if event.key == 1073741904: #flecha izquierda
                colorear((200,100,150))

            if event.key == 1073741903: #flecha derecha
                colorear((10,150,200))
pygame.quit()

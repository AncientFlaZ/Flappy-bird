import pygame,sys,random

def draw_base():
    screen.blit(base_surface,(base_x_pos,450))
    screen.blit(base_surface,(base_x_pos + 288,450))



pygame.init()

screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

bg_surface = pygame.image.load('assets/background-day.png')
#bg_surface = pygame.transform.scale2x(bg_surface)
base_surface = pygame.image.load('assets/base.png')
base_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_surface,(0,0))
    base_x_pos -=1
    draw_base()
    if base_x_pos <= -288:
        base_x_pos = 0


    pygame.display.update()
    clock.tick(120)

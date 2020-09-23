import pygame,sys,random

def draw_base():
    screen.blit(base_surface,(base_x_pos,450))
    screen.blit(base_surface,(base_x_pos + 288,450))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    new_pipe = pipe_surface.get_rect(midtop= (325,random_pipe_pos))
    new_top_pipe = pipe_surface.get_rect(midbottom= (325,random_pipe_pos -150))
    return new_pipe,new_top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)
        if pipe.bottom >=512:
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)


def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            game_over = pygame.image.load('assets/gameover.png')
            return False
    if bird_rect.top <=50 or bird_rect.bottom >=450:
        game_over = pygame.image.load('assets/gameover.png')
        return False
    return True


def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 5 ,1)
    return new_bird


pygame.init()

screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0
game_active = True

bg_surface = pygame.image.load('assets/background-day.png')
base_surface = pygame.image.load('assets/base.png')
base_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png')
bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface = pygame.image.load('assets/pipe-green.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1000)
pipe_height = [200,300,400]





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement += 5
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center =(50,256)
                bird_movement = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())






    screen.blit(bg_surface,(0,0))


    if game_active:
     bird_movement -= gravity
     rotated_bird = rotate_bird(bird_surface)
     bird_rect.centery -= bird_movement
     screen.blit(rotated_bird,bird_rect)
     game_active =check_collision(pipe_list)

     pipe_list = move_pipes(pipe_list)
     draw_pipes(pipe_list)


    base_x_pos -=1
    draw_base()
    if base_x_pos <= -288:
        base_x_pos = 0


    pygame.display.update()
    clock.tick(120)

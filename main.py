import pygame
import os

WIDTH,HEIGHT = 900,600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE Fight Game!")

WHITE = (255,255,255)
BLACK = (0,0,0)
BORDER = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH,SPACESHIP_HEIGHT = 55,40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('attach','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),90)


RED_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('attach','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),270)


def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x, red.y))
    #pygame.draw.rect(WIN,BLACK,yellow)
    #pygame.draw.rect(WIN,BLACK,red)

    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x < BORDER.x - VEL - yellow.width:  # RIGHT
        yellow.x += VEL
        #print(BORDER.x - yellow.x)
    if keys_pressed[pygame.K_w] and yellow.y -VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + yellow.height + VEL< HEIGHT - 15:  # DOWN
        yellow.y += VEL

def red_handle_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x > BORDER.x + 10 + VEL :  # LEFT
        red.x -= VEL
        #print (BORDER.x - red.x)
    if keys_pressed[pygame.K_RIGHT] and red.x + red.width + VEL < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + red.height +VEL < HEIGHT -15:  # DOWN
        red.y += VEL



def main():
    red = pygame.Rect(700,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100,300,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []


    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS :
                    bullet = pygame.Rect(
                        yellow.x+yellow.width,yellow.y+yellow.height/2,10,5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS :
                    bullet = pygame.Rect(
                        red.x, red.y + red.height / 2, 10, 5)
                    red_bullets.append(bullet)


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)

        handle_bullets(yellow.bullets, red_bullets,yellow,red)

        draw_window(red,yellow)

    pygame.quit()

if __name__ == "__main__":
    main()
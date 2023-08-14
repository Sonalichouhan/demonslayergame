import pygame
import os

WIDTH,HEIGHT= 900, 600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("first game")

WHITE=(255,255,255)
BLACK=(0,0,0)

BORDER=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

FPS = 60
velocity=5

SPACESHIP_WIDTH1,SPACESHIP_HEIGHT1=200,200
SPACESHIP_WIDTH2,SPACESHIP_HEIGHT2=100,200

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','tanjiro.png.png'))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH1,SPACESHIP_HEIGHT1)),360)

RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join('Assets','muzan.png.png'))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH2,SPACESHIP_HEIGHT2)),360)
def draw_window(red,yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.display.update()

def yellow_handle_movement(keys_pressed,yellow):
     if keys_pressed[pygame.K_a] and yellow.x-velocity >0:
            yellow.x -=velocity
     if keys_pressed[pygame.K_d] and yellow.x+velocity+ yellow.width < BORDER.x:
            yellow.x +=velocity
     if keys_pressed[pygame.K_w]:
            yellow.y -=velocity
     if keys_pressed[pygame.K_s]:
            yellow.y +=velocity

def red_handle_movement(keys_pressed,red):
      if keys_pressed[pygame.K_LEFT]:
            red.x -=velocity
      if keys_pressed[pygame.K_RIGHT]:
            red.x +=velocity
      if keys_pressed[pygame.K_UP]:
            red.y -=velocity
      if keys_pressed[pygame.K_DOWN]:
            red.y +=velocity



def main():
    red=pygame.Rect(700,200,SPACESHIP_WIDTH2,SPACESHIP_HEIGHT2)
    yellow=pygame.Rect(100,200,SPACESHIP_WIDTH1,SPACESHIP_HEIGHT1)


    Clock=pygame.time.Clock()
    run = True
    while run:
        Clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        keys_pressed=pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed,red)
        
#help here
        draw_window(red,yellow)

    pygame.quit()

if __name__=="__main__":
    main()

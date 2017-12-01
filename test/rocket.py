# Author：TangWeiFeng
import pygame
import sys
import events

screen = pygame.display.set_mode((800,400))
bg_color = (0,0,250)
pygame.display.set_caption("星球大战")

image = pygame.image.load('images\ship.bmp')#图片宽60，高50(0--740,0--350)
#rect = image.get_rect()
#screen_rect = screen.get_rect()
#rect.centerx = screen_rect.centerx
#rect.bottom = screen_rect.bottom


zuobiao = events.Event(380,350)
zuobiao.events(380,350)
while True:
    #pygame.display.flip()
    #screen.fill(0, 0, 250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.fill(bg_color)
    screen.blit(image, (zuobiao.x,zuobiao.y))
    pygame.display.flip()




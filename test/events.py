# Author：TangWeiFeng
import pygame

class Event():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def events(self,x,y):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print ('1')

            elif event.type == pygame.KEYUP:
                print('q')
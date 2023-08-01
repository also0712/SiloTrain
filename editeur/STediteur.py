import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage

pygame.display.set_caption('SiloTrains - Map Editor')
clock = pygame.time.Clock()



class STediteur :
    def __init__(self,fenetre) :
        self.fenetre = fenetre
        
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            self.fenetre.fill((0,0,50))
            
            pygame.display.flip()
            clock.tick(60)
import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage






class STediteur :
    def __init__(self,fenetre,clock):
        self.fenetre = fenetre
        pygame.display.set_caption('SiloTrains - Map Editor')
        self.running=True
        self.clock = clock
        

        
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"

            self.fenetre.fill((0,0,50))
            
            pygame.display.flip()
            self.clock.tick(60)
import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage






class STediteur :
    def __init__(self):
        pygame.display.set_caption('SiloTrains - Map Editor')
        self.running=True
        

        
    def main_loop(self,env):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"

            env.fenetre.fill((0,0,50))
            
            pygame.display.flip()
            env.clock.tick(60)
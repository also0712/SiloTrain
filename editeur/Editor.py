import pygame
from pygame.locals import *
import os
import time
import copy
import commons.environnement.Environnement as Env



class Editor :
    def __init__(self):
        pygame.display.set_caption('SiloTrains - Map Editor')
        self.running=True
        

        
    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"

            Env.fenetre.fill((0,0,50))
            
            pygame.display.flip()
            Env.env.clock.tick(60)
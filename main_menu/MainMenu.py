import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MainMenu:
 
    def __init__(self,fenetre) :
        self.fenetre = fenetre
        pygame.display.set_caption('SiloTrains - Menu')
        self.running=True;

    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"

            self.fenetre.fill((0,0,50))
            
            pygame.display.flip()
            self.clock.tick(60)
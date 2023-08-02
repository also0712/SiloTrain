import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MainMenu:
 
    def __init__(self,fenetre,clock,textures) :
        self.clock = clock
        self.fenetre = fenetre
        self.textures = textures
        pygame.display.set_caption('SiloTrains - Menu')
        self.running=True
        self.pressed_keys = {}


    def main_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                    self.pressed_keys[event.key] = True #ajoute au dictionnaire si n'existe pas
                elif event.type == pygame.KEYUP:
                    self.pressed_keys[event.key] = False 



            self.fenetre.fill((0,0,50))   
            self.fenetre.blit(self.textures["Coal1"] ,(0, 0))         
            pygame.display.flip()
            self.clock.tick(60)
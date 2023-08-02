import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MainMenu:
 
    def __init__(self,fenetre,clock) :
        self.clock = clock
        self.fenetre = fenetre

        pygame.display.set_caption('SiloTrains - Menu')
        self.running=True
        self.pressed_keys = {
            1073741906 : False, #haut
            1073741905 : False, #bas
            1073741903 : False, #droite
            1073741904 : False  #gauche
        }


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
            pygame.display.flip()
            self.clock.tick(60)
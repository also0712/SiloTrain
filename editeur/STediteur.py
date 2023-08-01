import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage
pygame.init()
largeur_fenetre = 1280
hauteur_fenetre = 720
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption('editeur de map')
clock = pygame.time.Clock()
class STediteur:
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            fenetre.fill((0,0,50))
            
            pygame.display.flip()
            clock.tick(60)
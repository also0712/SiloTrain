import pygame
from pygame.locals import *
import os
import time
import copy
from editeur.STediteur import *
from main_menu.MainMenu import *

#================initialisation pygame
pygame.init()
clock = pygame.time.Clock()

#================initialisation fenetre
largeur_fenetre = 1280
hauteur_fenetre = 720
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))


#=============== gestion des game_mode ( )
running =True
mm = MainMenu(fenetre, clock)

while running : 
    game_mode = mm.main_loop() #la main loop du menu retour le mode de jeu

    if game_mode == "QUIT":
        pygame.quit;
        running = False

    if game_mode == "EDITOR":
        ed = STediteur(fenetre, clock)
        ed.main_loop()

    if game_mode == "GAME":
        pass
 
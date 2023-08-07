import pygame
from pygame.locals import *
import os
import time
import copy
from commons.Tools import *
from editeur.Editor import *
from main_menu.MainMenu import *
from Environnement import *



#================initialisation pygame
pygame.init()
            
enviro = Environment()


#=============== gestion des game_mode
running =True
main_menu = MainMenu(enviro)

while running : 
    game_mode = main_menu.main_loop(enviro) #la main loop du menu retour le mode de jeu

    if game_mode == "Quitter":
        pygame.quit
        running = False

    if game_mode == "Editeur":
        ed = Editor()
        ed.main_loop(enviro)

    if game_mode == "Jouer":
        pass
 
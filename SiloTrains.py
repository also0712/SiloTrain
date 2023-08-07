import pygame
from pygame.locals import *
import os
import time
import copy
from commons.Tools import *
from editeur.Editor import *
from main_menu.MainMenu import *
import commons.environnement.Environnement  as Env

#================initialisation pygame
pygame.init()

base_path = os.path.dirname(os.path.abspath(__file__))
Env.env = Env.Environment(base_path)

#=============== gestion des game_mode
running =True
main_menu = MainMenu()

while running : 
    game_mode = main_menu.main_loop() #la main loop du menu retour le mode de jeu

    if game_mode == "Quitter":
        pygame.quit
        running = False

    if game_mode == "Editeur":
        ed = Editor()
        ed.main_loop()

    if game_mode == "Jouer":
        pass
 
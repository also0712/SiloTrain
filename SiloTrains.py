import pygame
from pygame.locals import *
import os
import time
import copy
from commons.Tools import *
from editeur.STediteur import *
from main_menu.MainMenu import *

#================initialisation pygame
pygame.init()

clock = pygame.time.Clock()

#================initialisation fenetre
largeur_fenetre = 1280
hauteur_fenetre = 720
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

base_path = os.path.dirname(os.path.abspath(__file__))

#===============chargement des textures grounds
base_path_grounds = base_path + "\\assets\\grounds\\"
liste_fichier = os.listdir(base_path_grounds)

textures = {}
for file in liste_fichier:
    textures[file] = get_image(base_path_grounds + file ,112, 112)
    
    
#=============== gestion des game_mode
running =True
main_menu = MainMenu(fenetre, clock, textures)

while running : 
    game_mode = main_menu.main_loop() #la main loop du menu retour le mode de jeu

    if game_mode == "QUIT":
        pygame.quit
        running = False

    if game_mode == "EDITOR":
        ed = STediteur(fenetre, clock)
        ed.main_loop()

    if game_mode == "GAME":
        pass
 
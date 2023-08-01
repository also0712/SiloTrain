import pygame
from pygame.locals import *
import os
import time
import copy
from editeur.STediteur import *

pygame.init()
largeur_fenetre = 1280
hauteur_fenetre = 720
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

ed = STediteur(fenetre)

#appel de la loop principal de l'editeur
ed.main_loop()
#test
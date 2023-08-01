import pygame
from pygame.locals import *
import os
import time
import copy
from editeur.STediteur import *
pygame.init()
ed = STediteur()

#appel de la loop principal de l'editeur
ed.main_loop()
#test
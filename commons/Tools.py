import pygame
import os
from pygame.locals import *




# ======================================================================
#                    FONCTIONS COMMUNES REUTILISABLES PARTOUT
# ======================================================================
def get_image(file_name, widthDest, HeightDest, withAlpha):
    image = pygame.image.load(file_name)
    image = pygame.transform.scale(image, (widthDest, HeightDest))
    if (withAlpha==True):
        return image.convert_alpha()
    else:
        return image.convert()

# ======================================================================
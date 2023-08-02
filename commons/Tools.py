import pygame
import os
from pygame.locals import *




# ======================================================================
#                    FONCTIONS COMMUNES REUTILISABLES PARTOUT
# ======================================================================
def get_image(file_name, widthDest, HeightDest):
    global base_path
    image = pygame.image.load(file_name)
    image = pygame.transform.scale(image, (widthDest, HeightDest))
    return image


# ======================================================================
import pygame
import os
from pygame.locals import *
base_path = os.path.dirname(os.path.abspath(__file__))



# ======================================================================
#                    FONCTIONS COMMUNES REUTILISABLES PARTOUT
# ======================================================================
def get_image(file_name, widthDest, HeightDest):
    global base_path
    image = pygame.image.load(os.path.join(base_path, file_name))
    image = pygame.transform.scale(image, (widthDest, HeightDest))
    return image


# ======================================================================
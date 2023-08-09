import pygame
import os
from pygame.locals import *




# ======================================================================
#                    FONCTIONS COMMUNES REUTILISABLES PARTOUT
# ======================================================================
def get_image(full_file_name, withAlpha):
    image = pygame.image.load(full_file_name)
    if (withAlpha==True):
        return image.convert_alpha()
    else:
        return image.convert()
    

def is_in_rect(x, y , rect):
    p1_x = rect[0]
    p1_y = rect[1]
    p2_x = rect[2]
    p2_y = rect[3]
    
    if x < p1_x or y < p1_y or x > p2_x or y > p2_y:
        return False
    return True

# ======================================================================


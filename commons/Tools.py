import pygame
import os
from pygame.locals import *




# ======================================================================
#                    FONCTIONS COMMUNES REUTILISABLES PARTOUT
# ======================================================================
def get_image(file_name, withAlpha):
    image = pygame.image.load(file_name)
    if (withAlpha==True):
        return image.convert_alpha()
    else:
        return image.convert()
def is_in_rect(x_px, y_px , rect_px):
    p1_x = rect_px[0]
    p1_y = rect_px[1]
    p2_x = rect_px[2]
    p2_y = rect_px[3]
    
    if x_px < p1_x or y_px < p1_y or x_px > p2_x or y_px > p2_y:
        return False
    return True

# ======================================================================
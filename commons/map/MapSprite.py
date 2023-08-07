import pygame
from pygame.locals import *

import commons.environnement.Environnement as Env
from main_menu.MenuElement import *
from commons.Tools import *

class MapSprite:
    def __init__(self, name, num_row_cl, num_col_cl):
        self.sprite_name = name
        self.num_col_cl = num_col_cl
        self.num_row_cl = num_row_cl


    def draw(self):
        
        surf = Env.env.get_texture(self.sprite_name)
        
        positionX_pxl = Env.env.cell_width_pxl * self.num_col_cl
        positionY_pxl = Env.env.cell_width_pxl * self.num_row_cl
        Env.env.fenetre.blit( surf,(positionX_pxl, positionY_pxl)) 
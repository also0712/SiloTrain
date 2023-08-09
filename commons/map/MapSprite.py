import pygame
from pygame.locals import *

import commons.environnement.Environnement as Env
from main_menu.MenuElement import *
from commons.Tools import *

class MapSprite:
    def __init__(self, name, num_row_cel, num_col_cel):
        self.sprite_name = name
        self.num_col_cel = num_col_cel
        self.num_row_cel = num_row_cel
        self.rect_cel = None
        

    def draw(self):
        self.rect_cel = Env.env.blit_cel(self.sprite_name, self.num_row_cel,self.num_col_cel)
import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MenuElement:
 
    def __init__(self) :
        self.text=""
        self.x_nbcell = 0
        self.y_nbcell = 0
        self.is_selected=False
        self.color = (150,150,150) #gris
        self.color_selected = (200,200,200) #gris clair
        self.font = pygame.font.SysFont('Comic Sans MS', 30)


    def draw(self, env):
        
        color = self.color
        if self.is_selected:
            color = self.color_selected
        surf_elt = self.font.render(self.text, True, color)
        rect_element = surf_elt.get_rect()
        rect_element[0] = self.x_nbcell * env.cell_width_pxl
        rect_element[2] += self.x_nbcell * env.cell_width_pxl
        rect_element[1] = self.y_nbcell * env.cell_width_pxl
        rect_element[3] += self.y_nbcell * env.cell_width_pxl
        env.fenetre.blit(surf_elt, rect_element)
 

      

        

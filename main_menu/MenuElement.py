import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MenuElement:
 
    def __init__(self) :
        self.text=""
        self.x_pix = 0
        self.y_pix = 0
        self.is_selected=False
        self.color = (150,150,150) #gris
        self.color_selected = (200,200,200) #gris clair
        self.font = pygame.font.SysFont('Comic Sans MS', 50)

        self.surf_elt = self.font.render(self.text, True, self.color)
        


    def draw(self, env):
        
        color = self.color
        if self.is_selected:
            color = self.color_selected
        surf_elt = self.font.render(self.text, True, color)
        rect_element = surf_elt.get_rect()
        self.x_pix = env.largeur_fenetre_pxl // 2 - rect_element[2] // 2
        
        rect_element[0] = self.x_pix
        rect_element[1] = self.y_pix - rect_element[3]//2
        rect_element[2] += self.x_pix
        rect_element[3] += self.y_pix - rect_element[3] //2
        env.fenetre.blit(surf_elt, rect_element)
 

      

        

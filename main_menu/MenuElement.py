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
        self.rect_element = None
        self.surf_elt = None
    def preparation(self, env):
        
        color = self.color
        if self.is_selected:
            color = self.color_selected
        self.surf_elt = self.font.render(self.text, True, color)
        self.rect_element = self.surf_elt.get_rect()
        self.x_pix = env.largeur_fenetre_pxl // 2 - self.rect_element[2] // 2
        
        self.rect_element[0] = self.x_pix
        self.rect_element[1] = self.y_pix - self.rect_element[3]//2
        self.rect_element[2] += self.x_pix
        self.rect_element[3] += self.y_pix - self.rect_element[3] //2

    def draw(self, env):
        

        env.fenetre.blit(self.surf_elt, self.rect_element)
 

      

        

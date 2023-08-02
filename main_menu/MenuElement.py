import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MenuElement:
 
    def __init__(self) :
        self.text=""
        self.x=0
        self.y=0
        self.isSelected=False
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def setText(self,x,y,text):
        self.x =x
        self.y = y
        self.text = str(text)

    def setSelected(self,sel):
        self.isSelected = sel


    def draw(self):
        
        return  self.font.render(self.text, True, (0,0,0))
        #screen.blit(text, (x, y))
      

        

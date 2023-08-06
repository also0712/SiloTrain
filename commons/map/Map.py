import pygame
from pygame.locals import *
import os
import time
import copy
import random
from main_menu.MenuElement import *
from commons.Tools import *
from commons.map.MapSprite import *


class Map:
    
    def __init__(self, env):
        self.grounds = []
        self.over_grounds = []
        self.env = env
        
    def auto_generate_map(self):
        ground_texture_names = get_folder_files(self.env, "\\assets\\textures\\Grounds")
        cpt_cl = 0
        while cpt_cl < self.map_width_nbcell:
            alea = random.randint(0,len(ground_texture_names)-1)
            name = ground_texture_names[alea]
            map_sprite = MapSprite(name, cpt_cl*3)
            self.grounds.append(MapSprite)
            cpt_cl += 3
    
    def draw(self):
        for sprite in self.grounds:
            sprite.draw()
        
        
        
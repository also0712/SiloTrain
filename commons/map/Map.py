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
        
    def auto_generate_map(self,env):
        ground_texture_names = env.get_folder_files("\\assets\\textures\\Grounds\\")
        cpt_cel = 0
        while cpt_cel < env.map_width_cel:
            alea = random.randint(0,len(ground_texture_names)-1)
            name = ground_texture_names[alea]
            map_sprite = MapSprite(name, cpt_cel )
            self.grounds.append(map_sprite)
            cpt_cel += 3
    
    def draw(self,env):
        for sprite in self.grounds:
            sprite.draw(env)
        
        
        
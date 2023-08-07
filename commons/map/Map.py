
import pygame
import random
from pygame.locals import *
from main_menu.MenuElement import *
from commons.Tools import *
from commons.map.MapSprite import *
import commons.environnement.Environnement as Env

class Map:
    
    def __init__(self):
        self.grounds = []
        self.over_grounds = []
        
    def auto_generate_map(self):
        
        # =================auto génération des grounds =================
        ground_texture_names = Env.env.get_folder_files("\\assets\\textures\\Grounds\\")
        cpt_row_cel = 0
        while cpt_row_cel < Env.env.map_width_cel:
            cpt_col_cel = 0
            while cpt_col_cel < Env.env.map_width_cel:
                alea = random.randint(0,len(ground_texture_names)-1)
                name = ground_texture_names[alea]
                map_sprite = MapSprite(name, cpt_row_cel,cpt_col_cel )
                self.grounds.append(map_sprite)
                cpt_col_cel += 3
            cpt_row_cel += 3
        
    def draw(self):


        # ============== affichage des grounds ====================
        for sprite in self.grounds:
            sprite.draw()
        

        
        
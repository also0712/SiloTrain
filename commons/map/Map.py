
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
        
        # ================= auto génération des grounds =================
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
        
        # ================== auto génération des over grounds ==============
        
        over_ground_texture_names = Env.env.get_folder_files("\\assets\\textures\\OverGrounds\\")
        #nombre_de_mine = random.randint((Env.self.map_width_cel*Env.map_height_cel)//20,(Env.self.map_width_cel*Env.map_height_cel)//10)
        nombre_de_mine = 50
        for nb_mine in range(nombre_de_mine):
            alea = random.randint(0,len(over_ground_texture_names)-1)
            name = over_ground_texture_names[alea]
            mine_x_cel = random.randint(0,Env.env.map_width_cel)
            mine_y_cel = random.randint(0,Env.env.map_height_cel)
            map_sprite_over_grounds = MapSprite(name, mine_x_cel, mine_y_cel)
            self.over_grounds.append(map_sprite_over_grounds)
            
    def draw(self):

        # ============== affichage des grounds ====================
        for sprite in self.grounds:
            sprite.draw()
        for sprite in self.over_grounds:
            sprite.draw()
        

        
        
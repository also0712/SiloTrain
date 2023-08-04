import pygame
from pygame.locals import *
import os
import time
import copy
#import commons.GetImage


class MainMenu:
 
    def __init__(self) :
        pygame.display.set_caption('SiloTrains - Menu')
        self.running=True
        self.pressed_keys = {
            1073741906 : False, #haut
            1073741905 : False, #bas
            1073741903 : False, #droite
            1073741904 : False  #gauche
        }


    def main_loop(self,env):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYDOWN:
                    print(event.key)
                    self.pressed_keys[event.key] = True #ajoute au dictionnaire si n'existe pas
                elif event.type == pygame.KEYUP:
                    self.pressed_keys[event.key] = False 
                if event.type == MOUSEWHEEL:
                    env.change_zoom(-event.precise_y)

            self.draw_soil(env)
            self.draw_grid(env)
            pygame.display.flip()
            env.clock.tick(60)


    def draw_grid(self,env):
        num_row =0
        line_color = (240, 240, 240)
        while num_row < env.map_height_nbcell :
            posY_pxl = num_row * env.cell_width_pxl
            pygame.draw.line(env.fenetre, line_color, (0, posY_pxl), (env.largeur_fenetre_pxl, posY_pxl))
            num_row+=1

        num_col =0
        while num_col < env.map_width_nbcell :
            posX_pxl = num_col * env.cell_width_pxl
            pygame.draw.line(env.fenetre, line_color, (posX_pxl,0), (posX_pxl,env.hauteur_fenetre_pxl))
            num_col+=1


    def draw_soil(self,env):
        num_row =0
        while num_row < env.map_height_nbcell :
            self.draw_row_soil(env, num_row)
            num_row+=3


    def draw_row_soil(self,env,num_row):
        num_cell_horizontal =0
        
        while num_cell_horizontal < env.map_width_nbcell :
            positionX_pxl = num_cell_horizontal * env.cell_width_pxl
            positionY_pxl = num_row * env.cell_width_pxl
            txt=env.get_texture("Soil3.bmp")
           
            env.fenetre.blit( txt,(positionX_pxl, positionY_pxl)) 
           # env.fenetre.blit(env.textures["Coal1.png"] ,(positionX_pxl, positionY_pxl)) 
            num_cell_horizontal +=3 

        

        



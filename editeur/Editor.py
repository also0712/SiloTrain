import pygame
from pygame.locals import *
import os
import time
import copy
import commons.environnement.Environnement as Env
import commons.map.Map as Map


class Editor :
    def __init__(self):
        pygame.display.set_caption('SiloTrains - Map Editor')

        self.pressed_keys = {
            K_UP : False, #haut
            K_DOWN : False, #bas
            K_RIGHT : False, #droite
            K_LEFT : False  #gauche
        }

        self.map = Map.Map()
        self.map.generate_map_soil("Soil1.bmp")
        self.camera_cel= [0]*2
        
        
    def main_loop(self):
        while True:

            # ============================= gestion des imput clavier
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYDOWN:
                    self.pressed_keys[event.key] = True #ajoute au dictionnaire si n'existe pas
                elif event.type == pygame.KEYUP:
                    self.pressed_keys[event.key] = False 
                    
                if event.type == MOUSEWHEEL:
                    Env.env.change_zoom(-event.precise_y)

            cam_right_max_cel = Env.env.map_width_cel - Env.env.largeur_fenetre_pxl // Env.env.cell_width_pxl
            cam_down_max_cel = Env.env.map_height_cel - Env.env.hauteur_fenetre_pxl // Env.env.cell_width_pxl

            if self.pressed_keys[K_RIGHT]==True  and self.camera_cel[0] <cam_right_max_cel :
                self.camera_cel[0] +=0.1
            elif self.pressed_keys[K_LEFT]==True and self.camera_cel[0] >0 :
                    self.camera_cel[0] -=0.1
            if self.pressed_keys[K_UP]==True and self.camera_cel[1] >0:
                self.camera_cel[1] -=0.1
            elif self.pressed_keys[K_DOWN]==True and self.camera_cel[1] < cam_down_max_cel :
                self.camera_cel[1] +=0.1

            self.map.draw(self.camera_cel)

            
            pygame.display.flip()
            Env.env.clock.tick(60)
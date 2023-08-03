import pygame
from pygame.locals import *
import os
import time
import copy
from commons.Tools import *
from editeur.STediteur import *
from main_menu.MainMenu import *

#================initialisation pygame
pygame.init()


class Environment:
    def __init__(self) :
        self.clock = pygame.time.Clock()

        #================initialisation fenetre
        self.curent_zoom = 40
        self.max_zoom = 40
        self.min_zoom = 80
        self.largeur_fenetre_pxl = 1280
        self.hauteur_fenetre_pxl = 720
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre_pxl, self.hauteur_fenetre_pxl))

        self.cell_width_pxl = self.largeur_fenetre_pxl // self.curent_zoom  #on fait une division entiere pour ne pas a voir de fractions de pixel a gerer
        self.map_width_nbcell = 128
        self.map_height_nbcell = 64

        #===============chargement des textures
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.textures = {} #dictionnaire qui contiendra toutes les textures, la Key est le nom du fichier, et la key donne acces a une surface converted
    
    def change_zoom(self, zoom):
        if self.curent_zoom + zoom < self.max_zoom:
            return
        if self.curent_zoom + zoom  > self.min_zoom:
            return
        else:
            self.curent_zoom += zoom * 5
            print(self.curent_zoom)
            self.cell_width_pxl = self.largeur_fenetre_pxl // self.curent_zoom
            
                
    def load_textures(self, relative_folder, has_alpha,width_nbcel, height_nbcel ):
        full_dir = self.base_path + relative_folder
        lst_textures = os.listdir(full_dir)
        for file in lst_textures:
            if os.path.isfile(full_dir + file):
                self.textures[file] = get_image(full_dir + file ,
                                                width_nbcel  * self.cell_width_pxl, 
                                                height_nbcel * self.cell_width_pxl, 
                                                has_alpha)

enviro = Environment()
enviro.load_textures("\\assets\\grounds\\" , False,3,3)
enviro.load_textures("\\assets\\grounds\\OverGrounds\\", True, 3,3)

#=============== gestion des game_mode
running =True
main_menu = MainMenu()

while running : 
    game_mode = main_menu.main_loop(enviro) #la main loop du menu retour le mode de jeu

    if game_mode == "QUIT":
        pygame.quit
        running = False

    if game_mode == "EDITOR":
        ed = STediteur()
        ed.main_loop(enviro)

    if game_mode == "GAME":
        pass
 
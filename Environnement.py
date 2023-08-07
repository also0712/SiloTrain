import pygame
from pygame.locals import *
import os
import time
import copy
from commons.Tools import *


class Environment:
    def __init__(self) :
        self.clock = pygame.time.Clock()

        self.base_path = os.path.dirname(os.path.abspath(__file__))

        #================initialisation fenetre
        self.curent_zoom = 40
        self.max_zoom = 40
        self.min_zoom = 80
        self.largeur_fenetre_pxl = 1280
        self.hauteur_fenetre_pxl = 360
        self.fenetre = pygame.display.set_mode((self.largeur_fenetre_pxl, self.hauteur_fenetre_pxl))

        self.cell_width_pxl = self.largeur_fenetre_pxl // self.curent_zoom  #on fait une division entiere pour ne pas a voir de fractions de pixel a gerer
        self.map_width_cel = 128
        self.map_height_cel = 64

        #===============chargement des textures
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.textures = {} #dictionnaire qui contiendra toutes les textures, la Key est le nom du fichier, et la key donne acces a une surface converted

        self.load_textures("\\assets\\textures\\Grounds\\" , False)
        self.load_textures("\\assets\\textures\\OverGrounds\\", True)

    
    def get_folder_files(self,relative_folder ):
        full_dir = self.base_path + relative_folder
        return os.listdir(full_dir)

    def change_zoom(self, zoom):
        if  zoom>0 :
            zoom = 1
        elif  zoom<0 :
            zoom = -1
        if self.curent_zoom + zoom < self.max_zoom:# si on a atteind le zoom maximum donc au ne peut plus zoomer
            return
        if self.curent_zoom + zoom  > self.min_zoom: #si on a atteind le zoom minimum donc on ne peu plus dezoomer
            return
        else:
            self.curent_zoom += zoom * 5
            print(self.curent_zoom)
            self.cell_width_pxl = self.largeur_fenetre_pxl // self.curent_zoom #le zoom a changé on recalcule la taille d'une cellule de base (dont depent tous les autres graphisme)
   
        
    def load_textures(self, relative_folder, has_alpha ):
        full_dir = self.base_path + relative_folder
        lst_textures = self.get_folder_files(relative_folder)
        for file in lst_textures:
            if os.path.isfile(full_dir + file):
                self.textures[file] = get_image(full_dir + file , has_alpha)
    
    def get_texture(self, key):
        key_zoom = str(self.curent_zoom) + key
        if key_zoom in self.textures:
            return self.textures[key_zoom]
        else:
            txt = self.textures[key]
            print(txt.get_rect())
            width_pxl = txt.get_rect()[2]
            height_pxl = txt.get_rect()[3]
            height_cel = height_pxl // (self.largeur_fenetre_pxl // self.min_zoom) #nb cell pour le zoom de base
            width_cel = width_pxl // (self.largeur_fenetre_pxl // self.min_zoom)
            cell_dimension_pxl = self.largeur_fenetre_pxl // self.curent_zoom
            txt_scaled = pygame.transform.scale(txt, (cell_dimension_pxl * width_cel, cell_dimension_pxl * height_cel))
            print(txt_scaled.get_rect())
            if key.endswith('bmp'):
                self.textures[key_zoom]=txt_scaled.convert()
            elif key.endswith('png'):
                self.textures[key_zoom]=txt_scaled.convert_alpha()
            else:
                raise Exception("ERROR: le format d'image de " + key + " doit etre bmp ou png")
            
            return self.textures[key_zoom]
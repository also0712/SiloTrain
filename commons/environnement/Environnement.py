import pygame
from pygame.locals import *
import os
from commons.Tools import *

env=None

class Environment:
    def __init__(self,base_path) :
        self.clock = pygame.time.Clock()

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
        self.base_path = base_path 
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
        if self.curent_zoom + zoom < self.max_zoom: #si on a atteind le zoom maximum donc au ne peut plus zoomer
            return
        if self.curent_zoom + zoom  > self.min_zoom: #si on a atteind le zoom minimum donc on ne peu plus de-zoomer
            return
        else:
            self.curent_zoom += zoom * 5
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
            width_pxl = txt.get_rect()[2]
            height_pxl = txt.get_rect()[3]
            height_cel = height_pxl // (self.largeur_fenetre_pxl // self.min_zoom) #nb cell pour le zoom de base
            width_cel = width_pxl // (self.largeur_fenetre_pxl // self.min_zoom)
            cell_dimension_pxl = self.largeur_fenetre_pxl // self.curent_zoom
            txt_scaled = pygame.transform.scale(txt, (cell_dimension_pxl * width_cel, cell_dimension_pxl * height_cel))
            if key.endswith('bmp'):
                self.textures[key_zoom]=txt_scaled.convert()
            elif key.endswith('png'):
                self.textures[key_zoom]=txt_scaled.convert_alpha()
            else:
                raise Exception("ERROR: le format d'image de " + key + " doit etre bmp ou png")
            
            return self.textures[key_zoom]
    
    def blit_cel(self, sprite_name, row_cel, col_cel, camera_cel):

        surf = self.get_texture(sprite_name)
        positionX_pxl = self.cell_width_pxl * (col_cel - camera_cel[0])
        positionY_pxl = self.cell_width_pxl * (row_cel - camera_cel[1])
        rect = self.fenetre.blit( surf,(int(positionX_pxl), int(positionY_pxl)))

        #conversion pix =>  cel
        p2_x_cel = col_cel + (rect[2]-rect[0]) / self.cell_width_pxl
        p2_y_cel = row_cel + (rect[3]-rect[1]) / self.cell_width_pxl
        rect_cel = [col_cel,row_cel,p2_x_cel,p2_y_cel]
        return rect_cel
    
    def blit_line(self, line_color, p1_x_cel, p1_y_cel, p2_x_cel, p2_y_cel, camera_cel):

        # conversion cel en pix + decalage camera
        p1_x = self.cell_width_pxl * (p1_x_cel - camera_cel[0])
        p1_y = self.cell_width_pxl * (p1_y_cel - camera_cel[1])
        p2_x = self.cell_width_pxl * (p2_x_cel - camera_cel[0])
        p2_y = self.cell_width_pxl * (p2_y_cel - camera_cel[1])


        pygame.draw.line(env.fenetre, line_color, (p1_x, p1_y), (p2_x, p2_y))
        
import pygame
from pygame.locals import *
import os
import time
import copy
from main_menu.MenuElement import *



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
            
        self.menu_jouer = MenuElement()
        self.menu_editeur = MenuElement()
        self.menu_parametre = MenuElement()
        self.menu_quit = MenuElement()
        
        self.menu_jouer.text = "Jouer"
        self.menu_jouer.x_nbcell = 17
        self.menu_jouer.y_nbcell = 3
        self.menu_jouer.is_selected=True
        
        self.menu_editeur.text = "Editeur"
        self.menu_editeur.x_nbcell = 17
        self.menu_editeur.y_nbcell = 6
        self.menu_editeur.is_selected=False
        
        self.menu_parametre.text = "Parametre"
        self.menu_parametre.x_nbcell = 17
        self.menu_parametre.y_nbcell = 9
        self.menu_parametre.is_selected=False
        
        self.menu_quit.text = "Quitter"
        self.menu_quit.x_nbcell = 17
        self.menu_quit.y_nbcell = 12
        self.menu_quit.is_selected=False
        
        self.list_menu = [self.menu_jouer, self.menu_editeur ,self.menu_parametre ,self.menu_quit]
        
        self.quel_menu = 0
    
    def main_loop(self,env):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"
                elif event.type == pygame.KEYDOWN:
                    self.pressed_keys[event.key] = True #ajoute au dictionnaire si n'existe pas
                elif event.type == pygame.KEYUP:
                    self.pressed_keys[event.key] = False 
                    
                if event.type == MOUSEWHEEL:
                    env.change_zoom(-event.precise_y)
                if event.type == pygame.KEYDOWN:
                    if event.key == K_DOWN:
                        if self.quel_menu + 1 < len(self.list_menu):
                            self.quel_menu += 1
                    elif event.key == K_UP:
                        if self.quel_menu > 0:
                            self.quel_menu -= 1
                for mnu in self.list_menu:
                    mnu.is_selected = False
                self.list_menu[self.quel_menu].is_selected = True
             
            self.draw_soil(env)
            self.draw_grid(env) 
          
            for mnu in self.list_menu:
                mnu.draw(env)
                
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
            txt=env.get_texture("Soil2.bmp")
           
            env.fenetre.blit( txt,(positionX_pxl, positionY_pxl)) 
           # env.fenetre.blit(env.textures["Coal1.png"] ,(positionX_pxl, positionY_pxl)) 
            num_cell_horizontal +=3 

        

        



import pygame
from pygame.locals import *
import os
import time
import copy
from main_menu.MenuElement import *
from commons.Tools import *
from commons.map.Map import *


class MainMenu:
    
    def __init__(self, env) :
        pygame.display.set_caption('SiloTrains - Menu')
        self.running=True
        self.pressed_keys = {
            1073741906 : False, #haut
            1073741905 : False, #bas
            1073741903 : False, #droite
            1073741904 : False  #gauche
        }
            
        
        self.menu_jouer = MenuElement()
        self.menu_jouer.text = "Jouer"
        self.menu_jouer.is_selected=True
        
        self.menu_editeur = MenuElement()
        self.menu_editeur.text = "Editeur"
        self.menu_editeur.is_selected=False
        
        self.menu_parametre = MenuElement()
        self.menu_parametre.text = "Parametre"
        self.menu_parametre.is_selected=False
        
        self.menu_quit = MenuElement()
        self.menu_quit.text = "Quitter"
        self.menu_quit.is_selected=False
        
        self.list_menu = [self.menu_jouer, self.menu_editeur ,self.menu_parametre ,self.menu_quit]
        compteur = 0
        for menu in self.list_menu:
            compteur += 1
            espace = env.hauteur_fenetre_pxl // (len(self.list_menu) + 1)
            menu.y_pix = espace * compteur
        self.quel_menu = 0
    
    def main_loop(self,env):
        while self.running:
            return_key_pressed = False
            keyboard_changed = False
            
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
                            keyboard_changed = True
                    elif event.key == K_UP:
                        if self.quel_menu > 0:
                            self.quel_menu -= 1
                            keyboard_changed = True
                    elif event.key == K_RETURN :
                        return_key_pressed=True
                if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                    return_key_pressed=True
                mouse_x_px, mouse_y_px = pygame.mouse.get_pos()
                

                #======================calculs
                
               
                if return_key_pressed :
                    for mnu in self.list_menu: #detection si les felche nous envoie sur un menu
                        if mnu.is_selected :
                            return mnu.text

                
                
                for mnu in self.list_menu:
                    mnu.preparation(env)
                
                if keyboard_changed :
                    for mnu in self.list_menu: #detection si les felche nous envoie sur un menu
                        mnu.is_selected = False
                    self.list_menu[self.quel_menu].is_selected = True
                  
                else:
                    for mnu in self.list_menu: #detection si la souris est sur un menu
                        mouse_in_rect = is_in_rect(mouse_x_px, mouse_y_px , mnu.rect_element)
                        if mouse_in_rect == True:
                            for mnu2 in self.list_menu: 
                                mnu2.is_selected = False
                            mnu.is_selected = True
                            break
                
            #=========================affichage
            
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
        map = Map(env)
        map.draw()
       
        

        



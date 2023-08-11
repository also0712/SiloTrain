import pygame
import commons.environnement.Environnement as Env

from pygame.locals import *
from commons.map.Map import *
from main_menu.MenuElement import *
from commons.Tools import *


class MainMenu:
    
    def __init__(self) :
        
        pygame.display.set_caption('SiloTrains - Menu')
        self.running=True

            
        
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
            espace = Env.env.hauteur_fenetre_pxl // (len(self.list_menu) + 1)
            menu.y_pix = espace * compteur
        self.quel_menu = 0


        self.map = Map()
        self.map.auto_generate_map()
    
    def main_loop(self):
        global _env
        while self.running:
            return_key_pressed = False
            keyboard_changed = False
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    return "QUIT"

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
                
                if event.type == MOUSEWHEEL:
                    Env.env.change_zoom(-event.precise_y)
                
                mouse_x_px, mouse_y_px = pygame.mouse.get_pos()
                

                #======================calculs
                if return_key_pressed :
                    for mnu in self.list_menu: #detection si les felche nous envoie sur un menu
                        if mnu.is_selected :
                            return mnu.text

                for mnu in self.list_menu:
                    mnu.preparation()
                
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
            camera_fixe = [0]*2
            self.map.draw(camera_fixe)
           
          
            for mnu in self.list_menu:
                mnu.draw()
                
            pygame.display.flip()
            Env.env.clock.tick(60)
            
            
            

   

   
       


   
        
       
        

        



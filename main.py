import pygame as pg
from Utilites_game import draw_text, liczebniki
class Shop():
    def __init__(self,screen,sprite,Player,upgrade_group):
        self.screen=screen
        self.shop_activation=False
        self.player=Player
        self.Sprite=sprite
        self.shop_x=50
        self.text_font = pg.font.Font('robot.ttf',25)
        self.shop_y=79
        self.shop_w=1200
        self.shop_h=600
        self.shop_open=self.Sprite((screen.get_width()/2)-75,100,self.shop_w,self.shop_h,color=(234,217,149),opacity=235)
        self.buttons=pg.sprite.Group()
        self.button_group=[self.Sprite(220,150,img_path="button.png",change_to="button_clicked.png"),
                    self.Sprite(250,450,img_path="button.png",change_to="button_clicked.png"),
                    self.Sprite(920,150,img_path="button.png",change_to="button_clicked.png"),
                    self.Sprite(920,450,img_path="button.png",change_to="button_clicked.png"),
                    self.Sprite(600,300,img_path="button.png",change_to="button_clicked.png")
                    ]
        self.food_man=self.Sprite(100,100,116.5,176,img_path="food_man.png")
        self.gathering_food_man=self.Sprite(80,400,157.5,164,img_path="gathering_food_man.png")
        self.axe_man=self.Sprite(800,400,100.5,194.5,img_path="axe_man.png")
        self.spear_man=self.Sprite(770,90,137,169.5,img_path="spear_man.png")
        self.clicker_to_upgrade=self.Sprite((screen.get_width()/2)-200,260,w=150,h=150,img_path="clicker.png")

        for buttond in self.button_group:
            buttond.setting="upgrade"
            buttond.option="click"
    #### W tej sekcji ustawiam dane dla guzików 
        ### food man upgrade button
        if self.player.ulepszenia[0]:
            upgrade_group[1]=self.Sprite(200,425,116.5,176,img_path="food_man.png")
        self.button_group[0].times_zbiory=[1.09,1.2]
        if self.player.ulepszenia[0]:
            self.button_group[0].lvl=self.player.ulepszenia[0][0]
            self.button_group[0].cost=self.player.ulepszenia[0][1]
        else:
            self.button_group[0].cost=100
        self.button_group[0].option_needed_to_buy="food"
        ####
        
        #### gathering food man upgrade button
        if self.player.ulepszenia[1]:
            upgrade_group[2]=self.Sprite(screen.get_width()-270,500,157.5,164,img_path="gathering_food_man.png")
        self.button_group[1].times_zbiory=[1.19,1.3]
        self.button_group[1].id=1
        if self.player.ulepszenia[1]:
            self.button_group[1].lvl=self.player.ulepszenia[1][0]
            self.button_group[1].cost=self.player.ulepszenia[1][1]
        else:
            self.button_group[1].cost=1000
        self.button_group[1].option_needed_to_buy="food"
        ####

        #### axe man upgrade button
        if self.player.ulepszenia[2]:
            upgrade_group[3]=self.Sprite(screen.get_width()-270,275,137,169.5,img_path="spear_man.png")
        self.button_group[2].times_zbiory=[1.3,1.5]
        self.button_group[2].id=2
        if self.player.ulepszenia[2]:
            self.button_group[2].lvl=self.player.ulepszenia[2][0]
            self.button_group[2].cost=self.player.ulepszenia[2][1]
        else:
            self.button_group[2].cost=100000
        self.button_group[2].option_needed_to_buy="food"
        #### spear man upgrade button
        if self.player.ulepszenia[3]:
            upgrade_group[0]=self.Sprite(200,250,100.5,194.5,img_path="axe_man.png")
        self.button_group[3].times_zbiory=[1.49,1.7]
        self.button_group[3].id=3
        if self.player.ulepszenia[3]:
            self.button_group[3].lvl=self.player.ulepszenia[3][0]
            self.button_group[3].cost=self.player.ulepszenia[3][1]
        else:
            self.button_group[3].cost=100000
        self.button_group[3].option_needed_to_buy="wood"
        #### button upgrade
        self.button_group[4].times_zbiory=[1.3,4.25]
        self.button_group[4].id=4
        if self.player.ulepszenia[4]:
            self.button_group[4].lvl=self.player.ulepszenia[4][0]
            self.button_group[4].cost=self.player.ulepszenia[4][1]
        else:
            self.button_group[4].cost=1000
        self.button_group[4].option_needed_to_buy="food"
    def draw(self):

        ## tutaj rysuję sklep
        if self.shop_activation:
            self.buttons.add(self.button_group)
            self.screen.blit(self.shop_open.image,(self.shop_x,self.shop_y))
            self.screen.blit(self.food_man.image,self.food_man.rect.topleft)
            self.screen.blit(self.gathering_food_man.image,self.gathering_food_man.rect.topleft)
            self.screen.blit(self.spear_man.image,self.spear_man.rect.topleft)
            self.screen.blit(self.axe_man.image,self.axe_man.rect.topleft)
            self.screen.blit(self.clicker_to_upgrade.image,self.clicker_to_upgrade.rect.topleft)
            self.buttons.draw(self.screen)
            button_1_x,button_1_y=self.button_group[0].rect.topleft
            draw_text(self.screen,"lvl: "+ str(self.button_group[0].lvl),self.text_font,(0,0,0),button_1_x+80,button_1_y)
            draw_text(self.screen,"cost: "+ liczebniki(self.button_group[0].cost),self.text_font,(0,0,0),button_1_x+60,button_1_y+25)
            button_2_x,button_2_y=self.button_group[1].rect.topleft
            draw_text(self.screen,"lvl: "+ str(self.button_group[1].lvl),self.text_font,(0,0,0),button_2_x+80,button_2_y)
            draw_text(self.screen,"cost: "+ liczebniki(self.button_group[1].cost),self.text_font,(0,0,0),button_2_x+60,button_2_y+25)
            button_3_x,button_3_y=self.button_group[2].rect.topleft
            draw_text(self.screen,"lvl: "+ str(self.button_group[2].lvl),self.text_font,(0,0,0),button_3_x+80,button_3_y)
            draw_text(self.screen,"cost: "+ liczebniki(self.button_group[2].cost),self.text_font,(0,0,0),button_3_x+60,button_3_y+25)
            button_4_x,button_4_y=self.button_group[3].rect.topleft
            draw_text(self.screen,"lvl: "+ str(self.button_group[3].lvl),self.text_font,(0,0,0),button_4_x+80,button_4_y)
            draw_text(self.screen,"cost: "+ liczebniki(self.button_group[3].cost),self.text_font,(0,0,0),button_4_x+60,button_4_y+25)
            button_5_x,button_5_y=self.button_group[4].rect.topleft
            draw_text(self.screen,"lvl: "+ str(self.button_group[4].lvl),self.text_font,(0,0,0),button_5_x+80,button_5_y)
            draw_text(self.screen,"cost: "+ liczebniki(self.button_group[4].cost),self.text_font,(0,0,0),button_5_x+60,button_5_y+25)


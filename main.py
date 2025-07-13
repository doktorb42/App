import pygame as pg
import json
import os
import math
from sprite_load import Sprite
from shop_menu import Shop
from Utilites_game import draw_text,liczebniki
####################
#
#       W tej sekcji kodu użyłem biblioteczki json i os aby stworzyć folder odpowiedzialny do przechowywania danych po każdym zakończeniu gry.
#       Są tu przechowywane dane takie jak poziom czy ulepszenia zakupione przez gracza.
#
####################
data_json=""
try:
    with open('data/data_player.json', 'r') as file:
        data_json = json.load(file)
except:
    os.mkdir("data")
    data_json={"poziom": 0, "zbiory": 0, "drewno": 0, "ulepszenia": [[], [], [], [],[]]}
    out_file=open('data/data_player.json', 'w')
    json.dump(data_json,out_file)
####################
####################
#
#
#    Tutaj znajdują się podstawowe zmienne które ułatwiają wprowadzanie danych przy tworzenie obiektów w grze.
#    Przykładowo "screen" daje nam dane w jakich rozmiarach ma być nasze okno oraz "Run_game" daje nam opcję do sprawdzania czy gra jest uruchomiona czy nie
#
####################
Run_game=True
screen = pg.display.set_mode((1280,720))
##### shop settings
x_shop=screen.get_width()-240
y_shop=10
w_shop=230
h_shop=60
###

pg.init()
text_font = pg.font.Font('robot.ttf',32)
text_font_25 = pg.font.Font('robot.ttf',25)
clock = pg.time.Clock()
####################
####################
#
#
#    W tej sekcji stworzyłem klasę gracza abym mógł przechować niektóre dane związane np z poziomem czy też z ilością zebranych surowców.
#    Również tuyaj znajdują się funkcje które pozwalają na interakcję z obiektami w grze.
#
####################
class Player():
    def __init__(self):
        ############# Tutaj są dane potrzebne do przechowania.
        if data_json:
            self.poziom = data_json["poziom"]
            self.zbiory = data_json["zbiory"]
            self.ulepszenia = data_json["ulepszenia"]
            self.drewno = data_json["drewno"]
        else:
            self.poziom=0
            self.zbiory=0
            self.drewno=0
            self.ulepszenia=[[],[],[],[],[]]
        self.lastclicked=""
    def mouse_click(self,shop):
        ############# Tutaj jest funkcja która daje nam możliwość interakcji z obiektami w grze.    #####
        ### Przykładowo tutaj mamy warunek który sprawdza czy kliknęliśmy lewy przycisk myszki potem sprawdza w jaki obiekt myszką kliknęliśmy i gdy ten obiekt znajduję się w odpowiedniej grupie wtedy dodaje go do zmienej "lastclicked" aby wykonał inne działania.
        if pg.mouse.get_pressed()[0]==True:
            colision_group=None
            if pg.sprite.spritecollide(mouse,sprites,False):
                colision_group=pg.sprite.spritecollide(mouse,sprites,False,pg.sprite.collide_mask)
            elif pg.sprite.spritecollide(mouse,shop.button_group,False):
                colision_group=pg.sprite.spritecollide(mouse,shop.button_group,False,pg.sprite.collide_mask)
            if colision_group:
                if colision_group[0].option == "click":
                    if colision_group[0].setting == "clicker" and shop.shop_activation==False:
                        colision_group[0].update(1)
                        self.lastclicked=colision_group[0]
                    elif colision_group[0].setting != "clicker":
                        colision_group[0].update(1)
                        self.lastclicked=colision_group[0]
        ############ Tutaj mamy sekscje która sprawdza czy puściliśmy lewy przycisk myszki a następnie sprawdzamy czy obiekt odpowiedni został dodany do zmiennej "lastclicked" gdy to zostanie spełnione to wykonuje odpowienie działania np. dodaje +1 surowiec albo ulepsza nasz obiekt.
        else:
            if self.lastclicked!="":
                if self.lastclicked.change_image:
                    if self.lastclicked.punkty>0 and shop.shop_activation==False:
                        ### tutaj użyłem wzoru matematycznego aby po kliknięciu w przycisk dodwał odpowiedznią ilość surowca do naszego zbioru.
                        ### wzór:         ilość_punktów*poziom_obiektu^mnożnik_obiektu
                        ### przykładowo mamy obiekt który daje nam 1 surowiec, jego poziom to 4 lvl i obiektu mnożnik co lvl to jest 1.23
                        ### to ze wzoru wynika że dostaniemy 1*4^1.23  = 6
                        player.zbiory=player.zbiory+int(self.lastclicked.punkty*math.pow((1+shop.button_group[4].lvl),shop.button_group[4].times_zbiory[1]))
                    if self.lastclicked.setting == "shop":
                        if shop.shop_activation:
                            shop.shop_activation=False
                        else:
                            shop.shop_activation=True
                        if player.ulepszenia[0]:
                            if player.ulepszenia[0][0]==1:
                                upgrade_group[1]=Sprite(200,425,116.5,176,img_path="food_man.png")
                                upgrades.add(upgrade_group)
                        if player.ulepszenia[1]:
                            if player.ulepszenia[1][0]==1:
                                upgrade_group[2]=Sprite(screen.get_width()-270,500,157.5,164,img_path="gathering_food_man.png")
                                upgrades.add(upgrade_group)
                        if player.ulepszenia[2]:
                            if player.ulepszenia[2][0]==1:
                                upgrade_group[3]=Sprite(screen.get_width()-270,275,137,169.5,img_path="spear_man.png")
                                upgrades.add(upgrade_group)
                        if player.ulepszenia[3]:
                            if player.ulepszenia[3][0]==1:
                                upgrade_group[0]=Sprite(200,250,100.5,194.5,img_path="axe_man.png")
                                upgrades.add(upgrade_group)
                    if self.lastclicked.setting == "upgrade":
                        if self.lastclicked.option_needed_to_buy == "food":
                            if self.lastclicked.cost <= player.zbiory:
                                self.lastclicked.lvl+=1
                                player.zbiory=int(player.zbiory-self.lastclicked.cost)
                                self.lastclicked.cost=int(self.lastclicked.cost*math.pow(self.lastclicked.times_zbiory[0],self.lastclicked.lvl))
                                player.ulepszenia[self.lastclicked.id]=[self.lastclicked.lvl,self.lastclicked.cost]
                        if self.lastclicked.option_needed_to_buy == "wood":
                            if self.lastclicked.cost <= player.drewno:
                                self.lastclicked.lvl+=1
                                player.drewno=int(player.drewno-self.lastclicked.cost)
                                self.lastclicked.cost=int(self.lastclicked.cost*self.lastclicked.times_zbiory[0])
                                player.ulepszenia[self.lastclicked.id]=[self.lastclicked.lvl,self.lastclicked.cost]
                    self.lastclicked.update(2)
                    self.lastclicked.update(2)
                    self.lastclicked=""


############################################################
player=Player()
#################### Tutaj tworzę obiekt aby było łatwiej wykrywać myszkę.
mouse = Sprite(0,0,w=1,h=1,color="black")
############################################################
########## Tutaj Tworzę obiekty
########## Obiekty które mogę ulepszy potem aby dawały mi więcej surowców automatycznie
upgrade_group=[Sprite(200,250,100.5,194.5,img_path="axe_man.png",opacity=100),
              Sprite(200,425,116.5,176,img_path="food_man.png",opacity=100),
              Sprite(screen.get_width()-270,500,157.5,164,img_path="gathering_food_man.png",opacity=100),
              Sprite(screen.get_width()-270,275,137,169.5,img_path="spear_man.png",opacity=100)]
########## guzik aby otwierać sklep
shop=Shop(screen,Sprite,player,upgrade_group)
########## grupy aby zebrać wszystkie obiekty w jedno i aby niezajmowały dużo pamięci
background_group=pg.sprite.Group()
sprites=pg.sprite.Group()
upgrades=pg.sprite.Group()
########## 
########## obiekt do tła
tlo=Sprite(0,-200,img_path="tlo.png")
########## obiekt który daje nam surowce po kliknięciu
clicker=Sprite((screen.get_width()/2)-100,100,w=150,h=150,img_path="clicker.png",change_to="clicker_clicked.png")
########## obiekty na mapie
objects_map=[Sprite(100, 500,img_path="bush.png"),
             Sprite(400, 330,img_path="bush.png"),
             Sprite(screen.get_width()-150,600,img_path="bush.png"),
             Sprite(50,70,img_path="tree.png"),
             Sprite(screen.get_width()-190,70,img_path="tree.png"),
             Sprite((screen.get_width()/2)-100,450,200,200,img_path="fireplace.png"),
             Sprite((screen.get_width()/2)-230,20,78.5,55.5,img_path="food.png"),
             Sprite((screen.get_width()/2)-150,25,120,50,color=(255,238,169)),
             Sprite((screen.get_width()/2)+50,20,78.5,55.5,img_path="wood.png"),
             Sprite((screen.get_width()/2)+130,25,120,50,color=(255,238,169)),
             Sprite((screen.get_width()/2)+60,300,174.857,198.2857,img_path="house.png")]
########## obiekt który otwiera nam sklep
shop_button=Sprite(x_shop,y_shop,w_shop,h_shop,img_path="button.png",change_to="button_clicked.png")
############################################################
##############Tutaj ustawiam dane dla poszczególnych rzeczy
shop_button.option="click"
shop_button.setting="shop"
clicker.option="click"
clicker.setting="clicker"
clicker.punkty=1
slow=0
show=0
show_button=0



############################################################


###############dodaje obiekty do grupy

background_group.add(tlo)
background_group.add(objects_map)
upgrades.add(upgrade_group)
############################################################
###
###         Tutaj jest gówna pętla która zawiera wszyskie opcje potrzebne aby uruchomić grę.
###
############################################################
while Run_game:
    ### pętla do sprawdzania czy gra została zamknięta
    for event in pg.event.get():
        if event.type == pg.QUIT:
            Run_game=False
    player.mouse_click(shop)
    ######## Tutaj rysuje obiekty
    background_group.draw(screen)
    sprites.add(shop_button,clicker)
    mouse.update(3)
    sprites.draw(screen)
    upgrades.draw(screen)
    draw_text(screen,liczebniki(player.zbiory),text_font,(0,0,0),(screen.get_width()/2)-145,30)
    draw_text(screen,liczebniki(player.drewno),text_font,(0,0,0),(screen.get_width()/2)+135,30)
    draw_text(screen,"Shop",text_font,(0,0,0),x_shop+75,y_shop+10)
    shop.draw()
    ######## tutaj gdy mamy coś ulepszone to wyświetla nad jego głową ilę surowców nam daje
    if slow>=60:
        if player.ulepszenia[0]:
            player.zbiory=player.zbiory+int(1*math.pow((1+shop.button_group[0].lvl),shop.button_group[0].times_zbiory[1]))
        if player.ulepszenia[1]:
            player.zbiory=player.zbiory+int(100*math.pow((1+shop.button_group[1].lvl),shop.button_group[1].times_zbiory[1]))
        if player.ulepszenia[2]:
            player.zbiory=player.zbiory+int(10000*math.pow((1+shop.button_group[2].lvl),shop.button_group[2].times_zbiory[1]))
            player.drewno=player.drewno+int(1*math.pow((1+shop.button_group[2].lvl),shop.button_group[2].times_zbiory[1]))
        if player.ulepszenia[3]:
            player.drewno=player.drewno+int(100*math.pow((1+shop.button_group[3].lvl),shop.button_group[3].times_zbiory[1]))
        if not shop.shop_activation:
            show=30
            
        slow=0
    if not shop.shop_activation:
        if show>=0:
            if player.ulepszenia[0]:
                draw_text(screen,"+ "+ liczebniki(int(1*math.pow((1+shop.button_group[0].lvl),shop.button_group[0].times_zbiory[1]))),text_font_25,(0,0,0),230,400)
            if player.ulepszenia[1]:
                draw_text(screen,"+ "+ liczebniki(int(100*math.pow((1+shop.button_group[1].lvl),shop.button_group[1].times_zbiory[1]))),text_font_25,(0,0,0),1040,470)
            if player.ulepszenia[2]:
                draw_text(screen,"+ "+ liczebniki(int(10000*math.pow((1+shop.button_group[2].lvl),shop.button_group[2].times_zbiory[1]))),text_font_25,(0,0,0),1040,250)
            if player.ulepszenia[3]:
                draw_text(screen,"+ "+ liczebniki(int(100*math.pow((1+shop.button_group[3].lvl),shop.button_group[3].times_zbiory[1]))),text_font_25,(0,0,0),1040,470)
            show-=1

        if show_button>=0:
            if player.ulepszenia[4]:
                draw_text(screen,"+ "+ liczebniki(int(1*math.pow((1+shop.button_group[4].lvl),shop.button_group[4].times_zbiory[1]))),text_font_25,(0,0,0),(screen.get_width()/2)-65,75)
            show_button-=1
    slow+=1
    ##
    pg.display.flip()
    clock.tick(60)
############################################################
###
###             gdy zamknięmy grę to wszystkie nasze zostają zapisywane do pliku
###
############################################################
#save data
data_json["poziom"]=player.poziom
data_json["zbiory"]=player.zbiory
data_json["drewno"]=player.drewno
data_json["ulepszenia"]=player.ulepszenia
with open("data/data_player.json", "w") as fb:
    json.dump(data_json, fb)
pg.quit()
############################################################
############################################################
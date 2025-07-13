import pygame as pg
import os
load_img=[{}]

### pętla do wczytywania obrazów
for file in os.listdir("img/"):
    load_img.append({"surface":pg.image.load("img/"+file),"name":file})


### klasa do rysowania obiektów
class Sprite(pg.sprite.Sprite):
    def __init__(self, x, y, w=None, h=None, img_path=None, color=None,change_to=None,opacity=0):
        pg.sprite.Sprite.__init__(self)
        if img_path:
            for file in load_img:
                if img_path == file.get("name"):
                    self.image=file.get("surface")
            if w and h:
                self.image=pg.transform.scale(self.image,(w,h))
            self.image=self.image.convert_alpha()
        else:
            if w and h:
                self.image=pg.Surface((w,h))
            else:
                self.image=pg.Surface((50,50))
        if color:
            self.image.fill(color=color)
        if change_to:
            for file in load_img:
                if change_to == file.get("name"):
                    self.change_image=file.get("surface")
            if w and h:
                self.change_image=pg.transform.scale(self.change_image,(w,h))
            self.change_image=self.change_image.convert_alpha()
            self.def_img=self.image.copy()
        self.opacity=opacity
        self.option=None
        self.setting=""
        if self.opacity>0:
            self.image.set_alpha(opacity)
            if change_to:
                self.change_image.set_alpha(opacity)
                self.def_img.set_alpha(opacity)
        self.punkty=0
        self.times_zbiory=0
        self.cost=0
        self.lvl=0
        self.id=0
        self.option_needed_to_buy=""
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.mask = pg.mask.from_surface(self.image)
    def update(self,selection):
        match selection:
            case 1:
                #change image
                self.image=self.change_image
            case 2:
                #default image
                self.image=self.def_img
            case 3:
                x,y=pg.mouse.get_pos()
                self.rect.center=(x,y)
            case _:
                pass
    
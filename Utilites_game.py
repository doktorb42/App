
import pygame as pg

#### ta funkcja zmienia liczbę w tekst z odpowiednim przedrostkiem np. 1000 zmienia w 1 tys.
def liczebniki(liczba=0):
    ilosc=0
    while liczba>=1000:
        ilosc+=1
        liczba/=1000
    liczba=int(liczba)
    match ilosc:
        case 0:
            liczba=str(liczba)
        case 1:
            liczba=str(liczba)+" tys."
        case 2:
            liczba=str(liczba)+" mln."
        case 3:
            liczba=str(liczba)+" mld."
        case 4:
            liczba=str(liczba)+" bln."
        case 5:
            liczba=str(liczba)+" bld."
        case 6:
            liczba=str(liczba)+" tln."
        case 7:
            liczba=str(liczba)+" tld."
        case 8:
            liczba=str(liczba)+" kln."
        case 9:
            liczba=str(liczba)+" kld."
        case _:
            liczba=str(liczba)+" 10^"+ str(ilosc)
    return str(liczba)

#### ta funkcja rysuje tekst 
def draw_text(screen,text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x,y))
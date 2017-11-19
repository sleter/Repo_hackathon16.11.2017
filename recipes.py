import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import ListProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from Przepis import Przepis



class Recipes(Screen):
    przepis = Przepis()
    tab = przepis.losowyPrzepis()
    name_text = str(tab[0])
    ing_text = str(tab[1])
    rec_text = str(tab[2])
    name_texxt = ''
    if(name_text=='RYZ Z PIERSIA Z KURCZAKA I ZE SZPINAKIEM (4os)'):
        name_texxt = "pic1.png"
    elif(name_text=='NALESNIKI (8 szt)'):
        name_texxt = "pic2.png"
    elif(name_text=='KOTLET SCHABOWY Z ZIEMNIAKAMI (4os)'):
        name_texxt = "pic3.png"
    elif(name_text=='TAGLIATELLE W SOSIE SEROWYM (4os)'):
        name_texxt = "pic4.png"
    elif(name_text=='RYBA PO GRECKU (4os)'):
        name_texxt = "pic5.png"


    def back(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'connected'



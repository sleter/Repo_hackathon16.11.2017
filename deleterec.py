import kivy

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import ListProperty, StringProperty
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from Przepis import Przepis
import getname
import getname2

class DeleteRec(Screen):
    przepis = Przepis()
    tab = ListProperty()
    tab = [" "," "," "]


        #if self.a == 2:
            #Clock.unschedule(self.update)
            #self.a=0

    def on_enter(self):
        stri = str(getname.dishname)
        del self.tab[:]
        self.tab = self.przepis.znajdz_przepis(stri)
        name_text = str(self.tab[0])
        ing_text = str(self.tab[1])
        rec_text = str(self.tab[2])
        self.ids['name_text'].text = str(self.tab[0])
        self.ids['ing_text'].text = str(self.tab[1])
        self.ids['rec_text'].text = str(self.tab[2])

        #print("check")
        #Clock.schedule_interval(self.update, 1)

    def delete(self):
        self.przepis.usun_przepis(self.stri)
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'yourdishes'

    def back(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'yourdishes'



import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from Przepis import Przepis

class Connected(Screen):
    przepis = Przepis()
    tab = przepis.losowyPrzepis()
    name_text = str(tab[0])
    ing_text = str(tab[1])
    rec_text = str(tab[2])

    def disconnect(self):
        self.manager.transition=SlideTransition(direction = 'right')
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForms()

    def randomRec(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'recipes'

    def createRec(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'adddish'

    def yourRec(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'yourdishes'

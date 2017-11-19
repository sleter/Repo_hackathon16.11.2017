import kivy

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, SlideTransition
from Przepis import Przepis
import getuser
import getuser2

class Adddish(Screen):
    przepis = Przepis()
    name = StringProperty()
    ingredients = StringProperty()
    recipe = StringProperty()
    nameU = StringProperty()

    def add(self,nameT,ingredientsT,recipeT):
        self.name = nameT
        self.ingredients = ingredientsT
        self.recipe = recipeT
        self.nameU = getuser.username
        #print(self.nameU)

        self.przepis.stworz_przepis(self.name,self.ingredients,self.recipe,self.nameU)

        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'connected'

    def back(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'connected'





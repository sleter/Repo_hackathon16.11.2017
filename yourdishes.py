import kivy

from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.listview import ListItemButton
from Przepis import Przepis

import getuser
import getuser2
import getname
import getname2

class DishesListButton(ListItemButton):
    pass

class YourDishes(Screen):

    dishes_list = ObjectProperty()
    przepis = Przepis()
    dishes = ListProperty()

    def show(self):
        nameU = getuser.username
        self.dishes = self.przepis.mojePrzepisy(nameU)
        #print("check")
        for i in self.dishes:
            #print(i[1])
            stri = str(i[1])
            self.dishes_list.adapter.data.extend([stri])
            self.dishes_list._trigger_reset_populate()

    def tonext(self):
        if self.dishes_list.adapter.selection:
            selection = self.dishes_list.adapter.selection[0].text
            getname.init()
            getname2.stuff(selection)
            self.manager.transition = SlideTransition(direction='right')
            self.manager.current = 'deleterec'

    def back(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'connected'





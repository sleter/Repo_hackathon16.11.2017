# -*- coding: utf-8 -*-
import kivy
kivy.require('1.10.0')

from kivy.core.window import Window
from kivy.app import App
from kivy.config import Config
#from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
#from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty, StringProperty
from connected import Connected
from registration import Registration
from recipes import Recipes
from logowanie import LogIn
from adddish import Adddish
from yourdishes import YourDishes
from deleterec import DeleteRec
Window.clearcolor = (1, 1, 1, 1)


import getuser
import getuser2


Config.set('kivy','window_icon','ikonka.png')
userName = ""
logging = LogIn()
#class CoNaObiad(BoxLayout):
   #pass

class Login(Screen):
    def do_login(self, loginT, passwordT):
        app = App.get_running_app()

        app.username = loginT
        app.password = passwordT
        logging.login = app.username
        logging.password = app.password
        if logging.CheckUser():
            getuser.init()
            getuser2.stuff(app.username)

            self.manager.transition = SlideTransition(direction = 'left')
            self.manager.current = 'connected'
        else:
            print("Sie zjebalo")

    def add_user(self):

        self.manager.transition = SlideTransition(direction = 'right')
        self.manager.current = 'registration'

    def resetForms(self):
        self.ids['login_input'].text=""
        self.ids['password_input'].text=""


class LoginApp( App ):
    username = StringProperty()
    password = StringProperty()
    #logging.connection.close()

    def build(self):
        manager = ScreenManager()
        #getuser4.stuff(getuser.username)
        manager.add_widget(Login(name = 'login'))
        manager.add_widget(Connected(name = 'connected'))
        manager.add_widget(Registration(name = 'registration'))
        manager.add_widget(Recipes(name='recipes'))
        manager.add_widget(Adddish(name='adddish'))
        manager.add_widget(YourDishes(name='yourdishes'))
        manager.add_widget(DeleteRec(name='deleterec'))
        return manager

if __name__ == '__main__':
    M = LoginApp()
    M.run()
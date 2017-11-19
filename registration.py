import kivy

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, SlideTransition
from logowanie import LogIn

submit = LogIn()

class Registration(Screen):
    login = StringProperty()
    password = StringProperty()
    password2 = StringProperty()
    email = StringProperty()

    def submit_user(self, loginT, passwordT, password2T, emailT):
        if passwordT == password2T:
            self.login = loginT
            self.password = passwordT
            self.password2 = password2T
            self.email = emailT

            submit.CreateUser(self.login, self.password, self.email)

            self.manager.transition = SlideTransition(direction='left')
            self.manager.current = 'login'

        else:
            print("sie zjebalo")

    def back(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = 'login'

from kivy.app import App
from kivy.boxlayout import boxlayout
from kivy.properties import ObjectProprety
from kivy.uix.listview import ListItemButton

class UserLogin(ListItemButton):
    pass

class UserLogin(boxlayout):
    username_text_input = ObjectProprety()
    password_text_input = ObjectProprety()
    
    def user_login(self):
        pass

class UserLoginApp(App):
    def build(self):
        return UserLogin()

ulApp = UserLoginApp()
ulApp.run()
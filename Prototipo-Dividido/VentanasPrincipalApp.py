from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Principal(Screen):

    def mostrar(self):
        print("Menu Principal")

class VentanasPrincipalApp(App):

    def build(self):

        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Principal(name='principal'))
        return root

if __name__ == '__main__':
    VentanasPrincipalApp().run()
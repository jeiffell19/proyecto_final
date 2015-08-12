from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Maestria(Screen):
    def mostrar(self):
        print("Maestria- Menu Principal")

class VentanasMaestriaApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Maestria(name='maestria'))
        return root

if __name__ == '__main__':
    VentanasMaestriaApp().run()
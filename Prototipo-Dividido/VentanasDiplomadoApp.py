from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder




class Diplomado(Screen):
    def mostrar(self):
        print("Diplomado- Menu Principal")

class VentanasDiplomadoApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Diplomado(name='diplomado'))
        return root

if __name__ == '__main__':
    VentanasDiplomadoApp().run()
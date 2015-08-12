from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Facultades(Screen):
    def mostrar(self):
        print("Facultades-Menu Principal")

class VentanasFacultadesApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principales
        
        # #Pantallas sub-Principales
        root.add_widget(Facultades(name='facultades'))
        return root

if __name__ == '__main__':
    VentanasFacultadesApp().run()
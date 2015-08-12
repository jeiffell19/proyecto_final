from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder



class Lincenciatura(Screen):
    def mostrar(self):
        print("Lincenciatura- Menu Principal") 

class VentanasLincenciaturaApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principalesbb
        root.add_widget(Lincenciatura(name='lincenciatura'))
      
        return root

if __name__ == '__main__':
    VentanasLincenciaturaApp().run()
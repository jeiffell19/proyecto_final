from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class LincenciaturaPro(Screen):
    def mostrar(self):
        print("LincenciaturaPro-Menu Principal")


class VentanasLincenciaturaProApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principales        
        root.add_widget(LincenciaturaPro(name='lincenciaturaPro'))
        return root

if __name__ == '__main__':
    VentanasLincenciaturaProApp().run()
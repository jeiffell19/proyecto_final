#!/usr/bin/python
# -*- coding: 850 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

class Postgrado(Screen):
    def mostrar(self):
        print("Postgrado Menu Principal")

class VentanasPostgradoApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Postgrado(name='postgrado'))
        return root

if __name__ == '__main__':
    VentanasPostgradoApp().run()
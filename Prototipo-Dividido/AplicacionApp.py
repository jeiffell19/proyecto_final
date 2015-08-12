#!/usr/bin/env python
#coding: utf8 


from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder


#Ventanas Principales 
class Principal(Screen):
    pass
class Lincenciatura(Screen):
    def mostrar(self):
        print("Lincenciatura- Menu Principal") 

class LincenciaturaPro(Screen):
    def mostrar(self):
        print("LincenciaturaPro-Menu Principal")

class Maestria(Screen):
    def mostrar(self):
        print("Maestria- Menu Principal")
class Postgrado(Screen):
    def mostrar(self):
        print("Postgrado Menu Principal")

class Diplomado(Screen):
    def mostrar(self):
        print("Diplomado- Menu Principal")

#Ventanas Secundarias 
class Facultades(Screen):
    def mostrar(self):
        print("Facultades-Menu Principal")
class Facultades_arquitectura(Screen):
    """Facultades_arquitectura"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Carreras(Screen):
    def mostrar(self):
        print("Carreras-Menu Principal")

class AplicacionApp(App):

    def build(self):
        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Principal(name='principal'))
        root.add_widget(Lincenciatura(name='lincenciatura'))
        root.add_widget(LincenciaturaPro(name='lincenciaturaPro'))
        root.add_widget(Maestria(name='maestria'))
        root.add_widget(Postgrado(name='postgrado'))
        root.add_widget(Diplomado(name='diplomado'))
        #Pantallas sub-Principales
        root.add_widget(Facultades(name='facultades'))
        root.add_widget(Facultades_arquitectura(name='arquitectura'))
        root.add_widget(Carreras(name='carreras'))
        return root

if __name__ == '__main__':
    AplicacionApp().run()
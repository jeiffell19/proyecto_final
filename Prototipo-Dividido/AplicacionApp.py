#!/usr/bin/env python
#coding: utf8

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder

#Ventanas Principales
class Principal(Screen):
    pass
class Licenciatura(Screen):
    def mostrar(self):
        print("Licenciatura- Menu Principal")
class LicenciaturaPro(Screen):
    def mostrar(self):
        print("LicenciaturaPro-Menu Principal")
class Maestria(Screen):
    def mostrar(self):
        print("Maestria - Menu Principal")
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
class Facultades_ciencias_salud(Screen):
    """Facultades_ciencias_salud"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Facultades_derecho(Screen):
    """Facultades_derecho"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Facultades_gastronomia(Screen):
    """Facultades_gastronomia"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Facultades_ingenieria(Screen):
    """Facultades_ingenieria"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Carreras(Screen):
    def mostrar(self):
        print("Carreras-Menu Principal")
#maestria
class EmpresarialesMaestria(Screen):
    def mostrar(self):
        print("Empresariales - Menu Principal")
class InnovacionMaestria(Screen):
    def mostrar(self):
        print("Innovacion - Menu Principal")
class EducacionMaestria(Screen):
    def mostrar(self):
        print("Educacion - Menu Principal")
class DerechoMaestria(Screen):
    def mostrar(self):
        print("Derecho - Menu Principal")
class SistemaiMaestria(Screen):
    def mostrar(self):
        print("Sistema De Informacion - Menu Principal")
class SaludMaestria(Screen):
    def mostrar(self):
        print("Salud - Menu Principal")

class AplicacionApp(App):
    def build(self):
        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Principal(name='principal'))
        root.add_widget(Licenciatura(name='licenciatura'))
        root.add_widget(LicenciaturaPro(name='licenciaturaPro'))
        root.add_widget(Maestria(name='maestria'))
        root.add_widget(Postgrado(name='postgrado'))
        root.add_widget(Diplomado(name='diplomado'))
        #Pantallas sub-Principales
        root.add_widget(Facultades(name='facultades'))
        root.add_widget(Facultades_arquitectura(name='arquitectura'))
        root.add_widget(Facultades_ciencias_salud(name='salud'))
        root.add_widget(Facultades_derecho(name='derecho'))
        root.add_widget(Facultades_gastronomia(name='gastronomia'))
        root.add_widget(Facultades_ingenieria(name='ingenieria'))
        #maestria
        root.add_widget(EmpresarialesMaestria(name='empresarialesmaestria'))
        root.add_widget(InnovacionMaestria(name='innovacionmaestria'))
        root.add_widget(EducacionMaestria(name='educacionmaestria'))
        root.add_widget(DerechoMaestria(name='derechomaestria'))
        root.add_widget(SistemaiMaestria(name='sistemaimestria'))
        root.add_widget(SaludMaestria(name='saludmaestria'))
        root.add_widget(Carreras(name='carreras'))
        return root

if __name__ == '__main__':
    AplicacionApp().run()

#!/usr/bin/env python
#coding: utf8

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder
# from _CarrerasDB_local  import *

#Ventanas Principales
class Principal(Screen):
    pass
class Licenciatura(Screen):
    def mostrar(self):
        print("Licenciatura-Menu Principal") 
class LicenciaturaPro(Screen):
    def mostrar(self):
        print("LicenciaturaPro-Menu Principal")
class Maestria(Screen):
    def mostrar(self):
        print("Maestria y Postgrado-Menu Principal")
class Diplomado(Screen):
    def mostrar(self):
        print("Diplomado-Menu Principal")
#Ventanas Secundarias
class Facultades(Screen):
    def mostrar(self):
        print("Facultades-Menu Principal")
class Facultades_arquitectura(Screen):
    """Facultades_arquitectura"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Facultades_ciencias_administrativas(Screen):
	"""Facultades_ciencias_administrativas"""
	def mostrar(self):
		print("facultades-Menu Principal")
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
class Facultades_maritima(Screen):
    """Facultades_maritima"""
    def mostrar(self):
        print("Facultades-Menu Principal")
class Carreras(Screen):
    def mostrar(self):
        print("Carreras-Menu Principal")
        # Limpiar campos 
        self.titulo=""
        self.resolucion=""
        self.duracion=""
        self.sede=""
        self.horario=""
        self.modalidad=""
        
    def carrera(self, resolucio):
        self.busqueda = ""+resolucio
        print("funcion para : ",self.busqueda )
        # informacion ={'Lic. en Ingeniería en Sistemas Computacionales':["CACAD-R-03-2009 / 05-Junio","4 años","Campus UIP y La Chorrera","Diurno y Nocturno","Presencial"]}
        valor=DbCarreras(self.busqueda )
        
        if self.busqueda  in valor:
            print(self.busqueda )
            print("si esta DISPONIBLE")
            for i in range (len(valor)):
                if i==0:
                    print("\t Carrera: ",valor[i])
                    self.titulo= valor[i]
                if i==1:
                    print("\t Resolución: ",valor[i])
                    self.resolucion= valor[i]
                if i==2:
                    print("Duración: ",valor[i])
                    self.duracion= valor[i]
                if i==3:
                    print("Sede: ",valor[i])
                    self.sede= valor[i]
                if i==4:
                    print("Horario: ",valor[i])
                    self.horario= valor[i]
                if i==5:
                    print("Modalidad: ",valor[i])
                    self.modalidad= valor[i]
        else:
            print("no esta DISPONIBLE")
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
class Ventanas(ScreenManager):
    nom =""
    def mostrar(self):
        print("Facultades-Menu Principal")
class PantallaApp(App):
    def build(self):
        return Ventanas()
class AplicacionApp(App):
    def build(self):
        root = ScreenManager()
        #Pantallas principales
        root.add_widget(Principal(name='principal'))
        root.add_widget(Licenciatura(name='licenciatura'))
        root.add_widget(LicenciaturaPro(name='licenciaturaPro'))
        root.add_widget(Maestria(name='maestria y postgrado'))
        root.add_widget(Diplomado(name='diplomado'))
        #Pantallas sub-Principales
        root.add_widget(Facultades(name='facultades'))
        root.add_widget(Facultades_arquitectura(name='arquitectura'))
        root.add_widget(Facultades_ciencias_administrativas(name='cadministrativa'))
        root.add_widget(Facultades_ciencias_salud(name='salud'))
        root.add_widget(Facultades_derecho(name='derecho'))
        root.add_widget(Facultades_gastronomia(name='gastronomia'))
        root.add_widget(Facultades_ingenieria(name='ingenieria'))
        root.add_widget(Facultades_maritima(name='maritima'))
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
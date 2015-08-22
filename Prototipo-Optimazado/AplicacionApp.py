#!/usr/bin/python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from _CarrerasDB_local  import *

class Ventanas(ScreenManager):
    nom =""
    def datos(self,ventana, Resolucion):
        # Limpiar campos 
        self.nom = Resolucion
        self.nombreVentana=ventana
        print(ventana," ====> ",Resolucion)

    def limpiar(self):
        self.titulo=""
        self.resolucion=""
        self.duracion=""
        self.sede=""
        self.horario=""
        self.modalidad=""
        print("Limpiando Variables") 

    def carrera(self):
        print("test: ",self.nom)

        self.busqueda = ""+self.nom
        print("funcion para : ",self.busqueda )

        # Realizando Consulta y Asignando el resultado de la Consulta
        valor=DbCarreras(self.busqueda )

        #Asignacion de los Datos Traidos  a la Ventana
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
                if i==6:
                    print("imagen requerimiento: ",valor[i])
                    self.requerimiento= valor[i]
                if i==7:
                    print("imagen plan: ",valor[i])
                    self.plan= valor[i]
        else:
            print("no esta DISPONIBLE")
    
class AplicacionApp(App):
	def build(self):
		return Ventanas()


if __name__ == '__main__':
	AplicacionApp().run()
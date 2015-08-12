# -*- coding: UTF-8 *-*
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

class Carreras(Screen,BoxLayout):
    def mostrar(self):
        print("Carreras-Menu Principal")
    def carrera(self, name):
        self.texto=name
        print("funcion para : "+name)
        informacion ={'Lic. en Ingeniería en Sistemas Computacionales':["CACAD-R-03-2009 / 05-Junio","4 años.","Campus UIP y La Chorrera.","Diurno y Nocturno.","Presencial"]}
        contenido=[]
        if name  in informacion:
            print("si esta DISPONIBLE")
            for clave,valor in informacion.items():
                contenido.append("\t Carrera: "+clave)
                print("\t Carrera: ",clave)
                for i  in range(len(valor)):
                    if i==0:
                    	print("\t Resolución: ",valor[i])
                    	contenido.append("\t Resolución: "+valor[i])
                    if i==1:
                    	print("Duración: ",valor[i])
                    	contenido.append("\t Duración: "+valor[i])
                    if i==2:
                    	print("Sede: ",valor[i])
                    	contenido.append("\t Sede: "+valor[i])
                    if i==3:
                    	print("Horario: ",valor[i])
                    	contenido.append("\t Horario: "+valor[i])
                    if i==4:
                    	print("Modalidad: ",valor[i])
                    	contenido.append("\t Modalidad: "+valor[i])
        else:
        	print("no esta DISPONIBLE")

        	contenido=["NO DISPONIBLE"]
        self.search_results.item_strings = contenido    

class VentanasCarrerasApp(App):
	icon = 'icon.png'
	title = 'Carreras'
	def build(self):
		root = ScreenManager()
		root.add_widget(Carreras(name='carreras'))
		return root

if __name__ == '__main__':
    VentanasCarrerasApp().run()
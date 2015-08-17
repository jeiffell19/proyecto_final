#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 

def DbCarreras(linciatura): 
    contenido =[]
    con = None  
    try:
        con = sqlite3.connect('bd_lincenciaturas')    
        cur = con.cursor()    
        # cur.execute('SELECT * FROM Carrera')
        consulta= ("SELECT * FROM Carrera WHERE resolucion LIKE '{}'".format(linciatura))
        cur.execute(consulta)
        datos = cur.fetchone()
        if datos == None:
            print("-No disponible-")
        else:           
            print("-Disponible-")
            for i  in range(len(datos)):
                if i==0:
                    # print("  Resolución: ",datos[i])
                    contenido.append(datos[i])
                if i==1:
                    # print("Duración: ",datos[i])
                    contenido.append(datos[i])
                if i==2:
                    # print("Sede: ",datos[i])
                    contenido.append(datos[i])
                if i==3:
                    # print("Horario: ",datos[i])
                    contenido.append(datos[i])
                if i==4:
                    # print("Modalidad: ",datos[i])
                    contenido.append(datos[i])
                    # print(contenido)
                if i==5:
                    # print("Modalidad: ",datos[i])
                    contenido.append(datos[i])
                    # print(contenido    
    except Exception as e: 
        print("Error %s : "%(e.args[0]) )
    finally:
        if con:
            con.close()
    return contenido

# lic= '123456'
# print(DbCarreras(lic))

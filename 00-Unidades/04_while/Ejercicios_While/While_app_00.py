import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 
# Procesamiento de lenguaje natural (NLP).

Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.








Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!2) - Tecnología que mas se votó.
    #!3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        seguir_ingresando = True

        contador_ia = 0
        contador_rv_ra = 0
        contador_iot = 0

        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0


        while seguir_ingresando == True:
            nombre = prompt("", "Ingrese su nombre: ")
            edad = prompt("", "Ingrese su edad: ")
            edad = int(edad)
            genero = prompt("","Ingrese su genero: ")
            tecnologia = prompt("","Ingrese su tecnologia deseada (IA, RV/RA, IOT,): ")

            while edad < 18:
                edad = prompt("","Reingrese su edad: ")
                edad = int(edad)
            
            while genero != "masculino" and genero != "femenino" and genero != "otro":
                genero = prompt("","Reingrese su genero: ")

            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT": 
                tecnologia = prompt("","Reingrese su tecnologia deseada (IA, RV/RA, IOT,): ")

            seguir = question("UTN", "Desea seguir ingresando?")
            
            match tecnologia:
                case "IA":
                    contador_ia += 1
                case "RV/RA":
                    contador_rv_ra += 1
                case _:
                    contador_iot += 1

            match genero:
                case "masculino":
                    contador_masculino += 1
                case "femenino":
                    contador_femenino
                case _:
                    contador_otro += 1


        










        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

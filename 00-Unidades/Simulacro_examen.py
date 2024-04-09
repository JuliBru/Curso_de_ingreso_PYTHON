import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Julieta
apellido: Bruzzo
---

---
Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. 
Para ello se ingresa por cada ganador:

-Nombre
-Importe ganado (mayor o igual $1000)
-Género (“Femenino”, “Masculino”, “Otro”)
-Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

Promedio de importe ganado de las personas que NO jugaron Poker, siempre y cuando el importe supere los $15000

Porcentaje de dinero en función de cada juego

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir_ingresando = True
        maximo_ganado = 0
        bandera_primero_importe = 0
        nombre_maximo_ganador = ""
        genero_maximo_ganador = ""
        
        acumulador_poker = 0
        acumulador_tragamonedas = 0
        acumulador_ruleta = 0
        acumulador_general = 0
        contador_ruleta = 0

        contador_juegos_general = 0
        contador_tragamonedas = 0
        contador_poker = 0
        contador_ruleta = 0

        importe_ruleta_tragamonedas = 0

        while seguir_ingresando == True:
            nombre = prompt("UTN","Ingrese su nombre:")
            importe_ganado = prompt("UTN","Ingrese el importe ganado:")
            importe_ganado = int(importe_ganado)
            genero = prompt("UTN","Ingrese el genero (Masculino, Femenino, Otro):")
            juego = prompt("UTN","Ingrese el juego (Ruleta, Poker, Tragamonedas):")



            while importe_ganado < 1000:
                importe_ganado = prompt("UTN","Reigrese el importe ganado:")
                importe_ganado = int(importe_ganado)

            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("UTN","Reigrese el genero (Masculino, Femenino, Otro):")

            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("UTN","Reigrese el juego (Ruleta, Poker, Tragamonedas):")

            contador_juegos_general += 1
            acumulador_general += importe_ganado

            seguir_ingresando = question("UTN", "¿Desea seguir ingresando?")


            if importe_ganado > maximo_ganado or bandera_primero_importe == True:
                maximo_ganado = importe_ganado
                nombre_maximo_ganador = nombre
                genero_maximo_ganador = genero
                bandera_primero_importe = False

            match juego:
                case "Ruleta":
                    acumulador_ruleta += importe_ganado
                    contador_ruleta += 1
                    if importe_ganado > 15000:
                        importe_ruleta_tragamonedas += importe_ganado


                case "Poker":
                    acumulador_poker += importe_ganado
                    contador_poker +=1


                case "Tragamonedas":
                    acumulador_tragamonedas += importe_ganado
                    contador_tragamonedas += 1
                    if importe_ganado > 15000:
                        importe_ruleta_tragamonedas += importe_ganado

        if contador_ruleta > 0:
            promedio_ruleta = acumulador_ruleta / contador_ruleta
            mensaje_promedio_ruleta = f"El promedio del dinero ganado en Ruleta es de: ${promedio_ruleta}"
        else: mensaje_promedio_ruleta = "El promedio del dinero ganado en Ruleta no se puede obtener"

        import math
        porcentaje_tragamonedas = (contador_tragamonedas * 100) / contador_juegos_general
        redondeo_porcentaje_tragamonedas = math.ceil(porcentaje_tragamonedas)

        if contador_ruleta < contador_poker and contador_ruleta < contador_tragamonedas:
            mensaje_menor_juego = "El juego menos elegido por los ganadores es la Ruleta"
        elif contador_poker < contador_tragamonedas:
            mensaje_menor_juego = "El juego menos elegido por los ganadores es el Poker"
        else: mensaje_menor_juego = "El juego menos elegido por los ganadores es el Tragamonedas"


        contador_ruleta_tragamonedas = contador_ruleta + contador_tragamonedas
        promedio_ruleta_tragamonedas = importe_ruleta_tragamonedas / contador_ruleta_tragamonedas

        porcentaje_ganado_ruleta = (acumulador_ruleta * 100) / acumulador_general
        redondeo_porcentaje_ganado_ruleta = math.ceil(porcentaje_ganado_ruleta)
        porcentaje_ganado_poker = (acumulador_poker * 100) / acumulador_general
        redondeo_porcentaje_ganado_poker = math.ceil(porcentaje_ganado_poker)
        porcentaje_ganado_tragamonedas = (acumulador_tragamonedas * 100) / acumulador_general
        redondeo_porcentaje_ganado_tragamonedas = math.ceil(porcentaje_ganado_tragamonedas)


        alert("UTN",f"{nombre_maximo_ganador} es el nombre del mayor ganador y su genero es {genero_maximo_ganador}")
        alert("UTN", mensaje_promedio_ruleta)
        alert("UTN", f"El porcentaje de personas que jugaron al Tragamonedas es el {redondeo_porcentaje_tragamonedas}% del total")
        alert("UTN", mensaje_menor_juego)
        alert("UTN", f"El promedio de importe ganado entre las personas que no jugaron al Poker es de: ${promedio_ruleta_tragamonedas}")
        alert("UTN", f"El {redondeo_porcentaje_ganado_ruleta}% del dinero ganado fue en la ruleta, {redondeo_porcentaje_ganado_poker}% del dinero ganado fue en el Poker y {redondeo_porcentaje_ganado_tragamonedas}% del dinero ganado fue en el Tragamonedas ")


        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

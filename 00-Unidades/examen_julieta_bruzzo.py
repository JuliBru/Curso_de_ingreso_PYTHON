import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter



'''

Nombre: Julieta
Apellido: Bruzzo
Division: TM-B
DNI: 47030366


De 5 mascotas que ingresan a una veterinaria se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M )
Edad(mayor a 0)


Pedir datos por prompt y mostrar por print, se debe informar:


Informe A XX- Cuál fue el tipo mas ingresado (gato ,perro o exotico)
Informe B XX- El porcentaje de mascotas femeninas y el de las masculinas.
Informe C XX- El tipo de la mascota más pesada
Informe D XX- El nombre del gato más joven
Informe E XX- El promedio de peso de todas las mascotas

'''




class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):

        contador_iteraciones = 0
        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0
        contador_f = 0
        contador_m = 0
        peso_maximo = 0
        edad_minima = 0
        acumulador_peso = 0



        while contador_iteraciones < 5:
            nombre = prompt("UTN", "Ingrese el nombre de su mascota")
            tipo = prompt("UTN", "Ingrese su tipo de mascota")
            peso = prompt("UTN", "Ingrese el peso de su mascota")
            peso = float(peso)
            sexo = prompt("UTN", "Ingrese el sexo de su mascota")
            edad = prompt("UTN", "Ingrese la edad de su mascota")
            edad = int(edad)


            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = prompt("UTN", "Reingrese su tipo de mascota (gato, perrro, exotico)")

            while peso < 10 or peso > 80:
                peso = prompt("UTN", "Reingrese el peso de su mascota (entre 10 y 80)")
                peso = float(peso)
            
            while sexo != "F" and sexo != "M":
                sexo = prompt("UTN", "Reingrese el sexo de su mascota (femenino (F), masculino(M))")

            while edad < 0:
                edad = prompt("UTN", "Reingrese la edad de su mascota (mayor a 0)")
                edad = int(edad)



            if peso > peso_maximo or contador_iteraciones == 0:
                peso_maximo = peso
                tipo_peso_max = tipo

        
            match sexo:
                case "F":
                    contador_f += 1
                case _:
                    contador_m += 1



            match tipo:
                case "gato":
                    contador_gato += 1
                    if edad < edad_minima or contador_iteraciones == 0:
                        edad_minima = edad
                        nombre_gato_joven = nombre
                case "perro":
                    contador_perro += 1
                case "exotico":
                    contador_exotico += 1

            acumulador_peso += peso
            contador_iteraciones += 1





        if contador_gato > contador_perro and contador_gato > contador_exotico:
            mensaje_1 = "El tipo de mascota más ingresado fue el gato"
        elif contador_perro > contador_exotico:
            mensaje_1 = "El tipo de mascota más ingresado fue el perro"
        else: mensaje_1 = "El tipo de mascota más ingresado fue el tipo exotico"

        porcentaje_f = (contador_f * 100) / contador_iteraciones
        redondeo_porcentaje_f = round(porcentaje_f)

        porcentaje_m = (contador_m * 100) / contador_iteraciones
        redondeo_porcentaje_m = round(porcentaje_m)

        promedio_peso_total = acumulador_peso / contador_iteraciones

        if contador_gato > 0:
            mensaje_2 = f"El nombre del gato más joven es: {nombre_gato_joven}" 
        else: mensaje_2 = "No se ingresó ninguna mascota tipo gato"

        print(mensaje_1)
        print(f"El porcentaje de mascotas femeninas ingresadas en total es el {redondeo_porcentaje_f}%\nEl porcentaje de mascotas masculinos ingresadas en total es el {redondeo_porcentaje_m}%")
        print(f"El tipo de mascota con mayor peso es {tipo_peso_max}")
        print(mensaje_2)
        print(f"El promedio del peso de todas las mascotas es de {promedio_peso_total}")


        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
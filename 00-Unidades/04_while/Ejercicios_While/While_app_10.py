import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        numero = 0
        suma_neg = 0
        suma_pos = 0
        contador_neg = 0
        contador_pos = 0
        ceros = 0
        diferencia = 0

        while True:
            numero = prompt("UTN", "Ingrese un numero")

            if numero == None:
                break
            
            numero = int(numero)

            if numero < 0:
                contador_neg += 1
                suma_neg += numero

            if numero > 0:
                contador_pos += 1
                suma_pos += numero
            
            if numero == 0: 
                ceros += 1

        if contador_pos > contador_neg:
            diferencia = contador_pos - contador_neg
        else:
            diferencia = contador_neg - contador_pos

        alert("UTN", f"La suma de los numeros negativos es = {suma_neg}, la suma de los numeros positivos es = {suma_pos}. En total se ingresaron {contador_neg} numeros negativos, {contador_pos} numeros positivios y un total de {ceros} ceros. La diferencia entre numeros positivos y negativos ingresados es de {diferencia}" ) 

        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

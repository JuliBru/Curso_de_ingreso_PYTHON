import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta de crédito y su edad promedio.
    #!          
    3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #!          
    4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
    #!          
    5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de  tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #!         
        6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
    #!          
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        seguir = True

        general = 16000
        campo = 25000
        platea = 30000

        contador_masc = 0
        contador_fem = 0
        contrador_otro = 0
        contador_personas_credito_general = 0
        contador_personas_debito_platea = 0
        contador_platea = 0

        contador_edades = 0
        contador_descuento_credito = 0
        bandera_primer_compra = True
        bandera_nros_primos = False
        nombre_primer_comprador = ""
        edad_primer_comprador = 0
        contador_platea_nro_primo = 0
        contador_total_platea_debito = 0

        
        

        while seguir == True:
            nombre = input("ingrese su nombre: ")
            edad = input("ingrese su edad: ")
            edad = int(edad)
            genero = input("ingrese su genero: ")
            tipo_de_entrada = input("ingrese el tipo de entrada que desea: ")
            medio_de_pago = input("ingrese el medio de pago: ")


            while edad < 16:
                edad = input("reingrese su edad: ")
                edad = int(edad)
            
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = input("reingrese su genero: ")

            while tipo_de_entrada != "General" and tipo_de_entrada != "Campo delantero" and tipo_de_entrada != "Platea":
                tipo_de_entrada = input("reingrese el tipo de entrada que desee: ")

            while medio_de_pago != "Credito" and medio_de_pago != "Debito" and medio_de_pago != "Else":
                medio_de_pago = input("reingrese su medio de pago deseado: ")





            match tipo_de_entrada:
                case "General":
                    if medio_de_pago == "Credito":
                        descuento = general * 0.20
                        precio_final = general - descuento
                        contador_descuento_credito += descuento
                        contador_personas_credito_general += 1
                        contador_edades += edad
                    elif medio_de_pago == "Debito":
                        descuento = general * 0.15
                        precio_final = general - descuento

                    if bandera_primer_compra == True:
                        nombre_primer_comprador = nombre
                        edad_primer_comprador = edad
                        bandera_primer_compra = False


                    if genero == "Masculino":
                        contador_masc += 1
                    elif genero == "Femenino":
                        contado += 1
                    else: contrador_otro += 1



                case "Campo delantero":
                    if medio_de_pago == "Credito":
                        descuento = campo * 0.20
                        precio_final = campo - descuento
                        contador_descuento_credito += descuento
                    elif medio_de_pago == "Debito":
                        descuento = campo * 0.15
                        precio_final = campo - descuento


                case "Platea":
                    for i in range (2, edad):
                        if edad % i == 0:
                            bandera_nros_primos = True
                        break

                    if bandera_nros_primos == False:
                        contador_platea_nro_primo += 1
                        



                    contador_platea += 1


                    if medio_de_pago == "Credito":
                        descuento = platea * 0.20
                        precio_final = platea - descuento
                        contador_descuento_credito += descuento
                    elif medio_de_pago == "Debito":
                        descuento = platea * 0.15
                        precio_final = platea - descuento
                        contador_personas_debito_platea += 1

                        if edad % 6 == 0:
                            contador_total_platea_debito += precio_final
                        




            print(f"Precio final de las entradas es de : ${precio_final}")

            seguir = question("SEGUIR", "¿Quiere seguir comprando entradas?")

                    


        if contador_masc > contador_fem and contador_masc > contrador_otro:
            mensaje_1 = "El genero que compro más entradas tipo campo es masculino"
        elif contador_fem > contrador_otro:
            mensaje_1 = "El genero que compro más entradas tipo campo es femenino"
        else: mensaje_1 = "El genero que compro más entradas tipo campo es otro"

        promedio_credito = 0

        if contador_personas_credito_general > 0:
            promedio_credito = contador_edades / contador_personas_credito_general
        else: promedio_credito = "no se puede relizar el promedio"

        promedio_platea = (contador_personas_debito_platea * 100) / contador_platea



        alert("UTN", mensaje_1)
        alert("UTN", f"En total compraron {contador_personas_credito_general} personas una entrada tipo Campo delantero mediante Credito y el promedio de edad es de: {promedio_credito} ")
        alert("UTN", f"En total compraron {contador_personas_debito_platea} personas entrada tipo Platea mediante Debito que esto representa un %{promedio_platea} del total. ")
        alert("UTN", f"El total de descuentos que se realizaron con el medio Credito es un total de ${contador_descuento_credito} pesos argentinos.")
        alert("UTN", f"El nombre del primer comprador de una entrada tipo General mediante Credito es: {nombre_primer_comprador} y su edad es de: {edad_primer_comprador} años")
        alert("UTN", f"En total {contador_platea_nro_primo} personas compraron entrada tipo Platea con edades primas.")
        alert("UTN", f"El total recaudado por las entradas tipo Platea mediante Debito y con personas que su edad eran multiplos de 6 es: ${contador_total_platea_debito}" )


            
    pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

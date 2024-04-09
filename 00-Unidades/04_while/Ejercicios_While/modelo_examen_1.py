import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:

    1) - Tipo de instrumento que menos se operó en total.
    2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    3) - Cantidad de usuarios que no compraron CEDEAR 
    4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    5) - Nombre y posicion del usuario que invirtio menos dinero
    6) - Promedio de dinero en CEDEAR  ingresado en total.  
    7) - Promedio de cantidad de instrumentos  MEP vendidos en total

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        '''
        contador_iteracion = 0

        contador_CEDEAR = 0
        contador_BONOS = 0
        contador_MEP = 0
        cantidad_MEP = 0

        no_compra_CEDEAR = 0

        bandera_primera_compra = True
        nombre_primer = ""
        cantidad_invertida_primer = 0

        total_CEDEAR = 0

        cantidad_instrumentos_MEP = 0

        monto_minimo = 0
        bandera_monto_minimo = True
        nombre_monto_minimo = ""
        contador_minimo = 0
        
        while contador_iteracion < 10:
            nombre = prompt("UTN", "Ingrese su nombre")

            monto_de_operacion = prompt("UTN", "Ingrese el monto deseado para la operación")
            monto_de_operacion = int(monto_de_operacion)

            tipo_instrumento = prompt("UTN", "Ingrese el tipo de instrumento (CEDEAR, BONOS, MEP)")
            
            cantidad_instrumentos = prompt("UTN", "Ingrese la cantidad de instrumentos que desea usar")
            cantidad_instrumentos = int(cantidad_instrumentos)

            contador_iteracion += 1


            while monto_de_operacion < 10000:
                monto_de_operacion = prompt("Error", "Reingrese un monto mayor a $10000 pesos")
                monto_de_operacion = int(monto_de_operacion)
            
            while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
                tipo_instrumento = prompt("Error", "Reingrese el tipo de instrumento valido (CEDEAR, BONOS, MEP) ")

            while cantidad_instrumentos < 0:
                cantidad_instrumentos = prompt("Error", "Reingrese la cantidad de instrumentos que desea usar")
                cantidad_instrumentos = int(cantidad_instrumentos)


            match tipo_instrumento:
                case "CEDEAR":
                    contador_CEDEAR +=1
                    total_CEDEAR += monto_de_operacion
                    if bandera_primera_compra == True:
                        nombre_primer = nombre
                        cantidad_invertida_primer = monto_de_operacion
                        bandera_primera_compra = False
                case "BONOS":
                    contador_BONOS += 1
                    no_compra_CEDEAR += 1
                    if bandera_primera_compra == True:
                        nombre_primer = nombre
                        cantidad_invertida_primer = monto_de_operacion
                        bandera_primera_compra = False
                case _:
                    if cantidad_instrumentos > 50 and cantidad_instrumentos < 200:
                        cantidad_MEP += 1
                    contador_MEP +=1
                    no_compra_CEDEAR += 1
                    cantidad_instrumentos_MEP += cantidad_instrumentos

            if monto_de_operacion < monto_minimo or bandera_monto_minimo == True:
                monto_minimo = monto_de_operacion
                nombre_monto_minimo = nombre
                contador_minimo = contador_iteracion


                

        if contador_CEDEAR < contador_BONOS and contador_CEDEAR < contador_MEP:
            mensaje_1 = "El intrumento menos usado es CEDEAR"
        elif contador_BONOS < contador_MEP:
            mensaje_1 = "El intrumento menos usado es BONOS"
        else: mensaje_1 = "El intrumento menos usado es MEP"

        promedio_CEDEAR = total_CEDEAR / contador_CEDEAR
        promedio_instrumentos_MEP = cantidad_instrumentos_MEP / contador_MEP

        alert("UTN", mensaje_1)
        alert("UTN", f"En total compraron {cantidad_MEP} personas entre 50 y 200 MEP")
        alert("UTN", f"En total hubieron {no_compra_CEDEAR} usuarios que no compraron CEDEAR")
        alert("UTN", f"El nombre del primer comprador de CEDEAR/BONOS es: {nombre_primer} e ingresó un monto de {cantidad_invertida_primer}")
        alert("UTN", f"El promedio de el monto total ingresado en CEDEAR es: {promedio_CEDEAR}")
        alert("UTN", f"El promedio de cantidad de instrumentos de MEP es: {promedio_instrumentos_MEP}")
        alert("UTN", f"El nombre de la persona que ingreso el menor monto es: {nombre_monto_minimo} y su posición fue la nro° {contador_minimo}")


        '''



        contador_iteracion = 0
        contador_cedear = 0
        contador_bonos = 0
        contador_mep = 0
        contador_50_200_mep = 0
        contador_no_cedear = 0
        bandera_primer_cedear_bonos = True
        monto_minimo = 0
        contador_minimo = 0
        acumulador_dinero_cedear = 0
        acumulador_instrumentos_mep = 0



        while contador_iteracion < 3:
            nombre = prompt("UTN", "Ingrese su nombre:")
            monto = prompt("UTN", "Ingrese el monto de la operacion:")
            monto = float(monto)
            instrumento= prompt("UTN", "Ingrese el instrumento que desea utilizar:")
            cantidad_instrumentos = prompt("UTN", "Ingrese la cantidad de instrumentos que desea comprar:")
            cantidad_instrumentos = int(cantidad_instrumentos)

            contador_iteracion += 1

            while monto < 10000:
                monto = prompt("UTN", "Reingrese el monto de la operacion:")
                monto = float(monto)

            while instrumento != "CEDEAR" and instrumento != "BONOS" and instrumento != "MEP":
                instrumento = prompt("UTN", "Reingrese el instrumento que desea utilizar (CEDEAR, BONOS, MEP):")

            while cantidad_instrumentos < 0:
                cantidad_instrumentos = prompt("UTN", "Reingrese la cantidad de instrumentos que desea comprar:") 
                cantidad_instrumentos = int(cantidad_instrumentos)


            if not instrumento == "CEDEAR":
                contador_no_cedear += 1

            if monto < monto_minimo or contador_iteracion == 1:
                monto_minimo = monto
                contador_minimo = contador_iteracion
                nombre_minimo = nombre


            match instrumento:
                case "CEDEAR":
                    contador_cedear += 1
                    acumulador_cedear += monto

                    if bandera_primer_cedear_bonos == True:
                        nombre_primer_cedear_bonos = nombre
                        monto_primer_cedear_bonos = monto
                        bandera_primer_cedear_bonos = False

                case "BONOS":
                    contador_bonos += 1 
                    if bandera_primer_cedear_bonos == True:
                        nombre_primer_cedear_bonos = nombre
                        monto_primer_cedear_bonos = monto
                        bandera_primer_cedear_bonos = False
                case "MEP":
                    contador_mep += 1
                    acumulador_instrumentos_mep += instrumento


                    if cantidad_instrumentos >= 50 and cantidad_instrumentos <= 200:
                        contador_50_200_mep += 1

                


        if contador_cedear < contador_bonos and contador_cedear < contador_mep:
            mensaje_1 = "El instrumento que menos se opero en total es CEDEAR "
        elif contador_bonos < contador_mep:
            mensaje_1 = "El instrumento que menos se opero en total es BONOS "
        else: mensaje_1 = "El instrumento que menos se opero en total es MEP "

        if contador_cedear > 0:
            promedio_cedear = acumulador_dinero_cedear / contador_cedear
            mensaje_2 = f"El promedio de dinero ingresado en CEDEAR es de: {promedio_cedear}"
        else: mensaje_2 = f"El promedio de dinero ingresado en CEDEAR es de: NO ES POSIBLE CALCULAR EL PROMEDIO"


        if contador_cedear > 0:
            promedio_mep = acumulador_instrumentos_mep / contador_mep
            mensaje_3 = f"El promedio de instrumentos MEP que se compraron es de: {promedio_mep}"
        else: mensaje_3 = f"El promedio de instrumentos MEP que se compraron es de: NO ES POSIBLE CALCULAR EL PROMEDIO"


        alert("UTN", mensaje_1)
        alert("UTN",f"En total {contador_50_200_mep} persona/s compraron entre 50 y 200 MEP")
        alert("UTN",f"En total {contador_no_cedear} persona/s no compraron CEDEAR")
        alert("UTN",f"El primer comprador de CEDEAR/BONOS se llama: {nombre_primer_cedear_bonos} e ingreso un monto de ${monto_primer_cedear_bonos}")
        alert("UTN",f"El nombre de la persona que invirtio menos dinero es: {nombre_minimo} y su posicion es la nro. {contador_minimo}")
        alert("UTN", mensaje_2)
        alert("UTN", mensaje_3)
        pass

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()

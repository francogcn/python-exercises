#! python3

#Importacion de modulos
import dolarhoy

#Se pide al usuario ingresar el monto a convertir
moneda = int(input("Ingrese el monto en pesos: "))

#El valor de la cotizacion se obtiene mediante un fetch del modulo dolarhoy
cotizacion = dolarhoy.get_dolarhoy()

#Se imprime el monto convertido
print(f"AR ${moneda} son U$D {moneda*cotizacion}")

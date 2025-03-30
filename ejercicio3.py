""" En la universidad del futuro, se necesita un programa con las siguientes caracteristicas

Ingresos
Deberá ingresar un monto
Descuentos
deberá ingresar un monto
Neto a pagar
Deberá calcular la Suma Total de Ingresos - Total de Descuentos

Se debe ingresar la cantidad de días No laborados """

#ENTRADA
ingreso = float(input("Digite el ingreso : "))
descuento = float(input("Digite el descuento : "))
diasNoLaborados = int(input("Digite la cantidad de días NO laborados : ")) 
descuentoRentaQuinta = int(input("Digite el descuento de renta de quinta : ")) 

# Digite el descuento de la 5ta Categoría
#PROCESO
pagoPorDia = ingreso / 30
diaLaborado = 30-diasNoLaborados
netoPagar = pagoPorDia - diaLaborado

#SALIDA
print("El Neto a pagar es: ", netoPagar)




#Variables
largo_pileta = float(input("Ingrese el largo de la pileta en metros: "))
ancho_pileta = float(input("Ingrese el ancho de la pileta en metros: "))
ancho_placa = 0.4
largo_placa = 0.4
precio_placa = 630

perimetro_total = 2 * (largo_pileta + ancho_pileta)
perimetro_piso = 2 * (largo_pileta - largo_placa) + 2 * (ancho_pileta - largo_placa)
metros_cuadrados = perimetro_piso * ancho_placa
metros_lineales = metros_cuadrados / largo_placa

#precio
num_placas = metros_cuadrados / (largo_placa * ancho_placa)
precio_total = num_placas * precio_placa

#Imprimir resultado
print("")
print("Metros lineales de placas necesarios:", metros_lineales)
print("")
print("Metros cuadrados de placas necesarios:", metros_cuadrados)
print("")
print("Número de placas necesarias:", num_placas)
print("")
print("Precio total de las placas: $", precio_total)
print("")
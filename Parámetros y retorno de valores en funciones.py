# #Hallar el valor a pagar de una compra sabiendo que hay descuento del 10%
# para todos los clientes y saber cual es el ahorro del descuento del 10% en la compra"
def calcular_descuento(total, descuento=10):
    descuento= (total * descuento)/100
    return descuento
monto_total= int(input("ingrese el valor:"))
descuento=calcular_descuento(monto_total)
monto_total=monto_total-descuento
print(f"monto total a pagar:{monto_total}")
print(f"descuento del 10%:{descuento}")

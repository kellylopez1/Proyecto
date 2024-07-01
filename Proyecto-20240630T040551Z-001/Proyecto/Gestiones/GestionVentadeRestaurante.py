from funciones import *
class GestionVentadeRestaurante:
    def __init__(self) -> None:
        pass

    def start(self, clientes):
        cedula = int(input("Ingrese su cedula: "))
        usuario = 0
        for cliente in clientes:
            if cliente.cedula == cedula:
                usuario = cliente
        if usuario != 0:
            if usuario.ticket.tipo == "VIP":
                productos = {}
                while True:
                    restaurante = escoger_Opcion(cliente.ticket.partido.estadio.restaurants)
                    producto = escoger_Opcion(restaurante.products)
                    cantidad = int(input("Ingrese la cantidad: "))
                    productos[producto] = cantidad
                    s = input("Presione 1 pagar continuar comprando o 2 para salir: ")
                    while s not in ["1", "2"]:
                        s = input("Presione 1 para continuar comprando o 2 para pagar: ")
                    if s == "2":
                        break
                total = 0
                for producto, cantidad in productos.items():
                    precio = float(producto.price) + float(producto.price)*0.16
                    total += precio
                    print(f"Producto {producto.name} Cantidad {cantidad} = {precio}")
                if self.perfecto(cliente.cedula):
                    print(f"SUBTOTAL A PAGAR {total}")
                    descuento = total * 0.15
                    total -=descuento
                    print(f"DESCUENTO POR CEDULA PERFECTA: {descuento}")

                
                print(f"TOTAL A PAGAR {total}")

                s = input("Presione 1 pagar continuar comprando o 2 para salir: ")
                while s not in ["1", "2"]:
                    s = input("Presione 1 pagar o 2 para cancelar: ")
                if s == "2":
                    return
                else:
                    for producto, cantidad in productos.items():
                        producto.vendido += cantidad
                        producto.stock -= cantidad
                        cliente.gastado += total
                    print("COMPRA REALIZADA CON EXITO")
    def perfecto(self, ci):
        suma = 0
        for i in range(1, ci):
            if ci % i == 0:
                suma += i
        return suma == ci
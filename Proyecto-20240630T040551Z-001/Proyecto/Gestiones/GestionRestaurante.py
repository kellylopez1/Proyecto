from Clases.Producto import Producto


class GestionRestaurante:
    def __init__(self, estadios : list) -> None:
        self.estadios = []

    def start(self): 
        while True:
            tipo = input("Ingrese el tipo de busqueda: (1) Por Nombre (2) Por Tipo (3) Por Precio: (4) Salir")
            while not tipo.isnumeric() or tipo not in ["1", "2", "3", "4"]:
                tipo = input("Ingrese el tipo de busqueda: (1) Por Nombre (2) Por Tipo (3) Por Precio: (4) Salir")
            if tipo == "1":
                self.buscar_producto_por_nombre(self.estadios)
            elif tipo == "2":
                self.buscar_producto_por_tipo(self.estadios)
            elif tipo == "3":
                self.buscar_producto_precio(self.estadios)
            else:
                return
    def buscar_producto_por_nombre(self, estadios):

        nombre = input("Ingrese el nombre del producto: ")
        for estadio in estadios:
            for restaurant in estadio.restaurants:
                for producto in restaurant.products:
                    if producto.name == nombre:
                       print( producto.__str__())

    def buscar_producto_por_tipo(self, estadios):

        tipo = input("Ingrese el tipo del producto: (1) Bebida (2) Alimento")
        while not tipo.isnumeric() or tipo not in ["1", "2"]:
            tipo = input("Ingrese el tipo del producto: (1) Bebida (2) Alimento")
        for estadio in estadios:
            for restaurant in estadio.restaurants:
                for producto in restaurant.products:
                    if (producto.adicional in ["alcoholic", "non-alcoholic"] and tipo == '1') or (producto.adicional not in ["alcoholic", "non-alcoholic"] and tipo == '2'):
                       print( producto.__str__())
                   
    
    def buscar_producto_precio(self, estadios):
        min = int(input("Ingrese el monto minimo : "))
        max = int(input("Ingrese el monto maximo: "))
        for estadio in estadios:
            for restaurant in estadio.restaurants:
                for producto in restaurant.products:
                    if min <= int(producto.price) <= max:
                       print( producto.__str__())


            

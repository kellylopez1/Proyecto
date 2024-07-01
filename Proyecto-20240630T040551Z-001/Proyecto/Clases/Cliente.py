class Cliente:
    def __init__(self, nombre: str, cedula: int, edad: int) -> None:
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.gastado = 0
        self.comprados = 0
        self.ticket = None

    def show_attr(self):
        return (f""" Ingrese sus datos para la compra de entradas:
                Nombre: {self.nombre}
                Cédula: {self.cedula}
                Edad:{self.edad}
                Partido que desea comprar ticket: {self.partido}
                Tipo de entrada: {self.tipo_entrada}
                
                """)
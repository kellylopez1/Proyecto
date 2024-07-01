from Clases.Partido import Partido


class Ticket:
    def __init__(self, tipo: str, precio: float, partido: Partido, posicion: list[int]) -> None:
        self.tipo = tipo
        self.precio = precio
        self.partido = partido
        self.posicion = posicion

        self.id = f"{partido.id}-{posicion[0]}-{posicion[1]}"
        self.asistencia = False

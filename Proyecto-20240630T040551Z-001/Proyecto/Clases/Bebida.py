from Clases.Producto import Producto


class Bebida(Producto):
    def __init__(self, name: str, quantity: int, price: float, stock: int, adicional: str) -> None:
        super().__init__("Bebida", name, quantity, price, stock, adicional)
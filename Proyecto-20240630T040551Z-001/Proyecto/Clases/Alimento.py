from Clases.Producto import Producto


class Alimento(Producto):
    def __init__(self, name: str, quantity: int, price: float, stock: int, adicional: str) -> None:
        super().__init__("Alimento", name, quantity, price, stock, adicional)
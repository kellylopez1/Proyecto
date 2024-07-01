from Clases.Producto import Producto


class Restaurant():
    def __init__(self, name: str, products: list[Producto]) -> None:
        self.name = name
        self.products = products

class Producto:
    def __init__(self, type: str, name: str, quantity: int, price: float, stock: int, adicional: str) -> None:
        self.type = type
        self.name = name
        self.quantity = quantity
        self.price = price
        self.stock = stock
        self.adicional = adicional
        self.vendido = 0

    def calcular_iva(self):
        iva = float(self.price) * 0.16
        return float(self.price) + iva

    def __str__(self):
        return f"Producto: {self.name}, Clasificación: {self.type}, Precio (IVA incluido): {self.calcular_iva()}"



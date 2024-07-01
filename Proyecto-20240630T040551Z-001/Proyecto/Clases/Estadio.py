from Clases.Restaurant import Restaurant


class Estadio():
    def __init__(self, id: str, name: str, city: str, capacity: list[int], restaurants: list[Restaurant]) -> None:
        self.id = id
        self.name = name
        self.city = city
        self.capacity = capacity
        self.restaurants = restaurants

    def __str__(self) -> str:
        return(F"""{self.name}
Ciudad: {self.city}""")
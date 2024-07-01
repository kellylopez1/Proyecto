class Equipo:
    def __init__(self, id: str, name: str, code: str, group: str) -> None:
        self.id = id
        self.name = name
        self.code = code
        self.group = group

    def __str__(self) -> str:
        return f"""{self.name} - {self.id}
Codigo: {self.code}
Group: {self.group}"""
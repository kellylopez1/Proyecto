from Clases.Equipo import Equipo
from Clases.Estadio import Estadio


class Partido:
    def __init__(self, id: str, number: int, date: str, group: str, stadium_Id:str, 
                home_Team: Equipo, away_Team: Equipo, estadio: Estadio) -> None:
        self.id = id
        self.number = number
        self.date = date
        self.group = group
        self.stadium_Id = stadium_Id
        self.home_Team = home_Team
        self.away_Team = away_Team
        self.estadio = estadio
        self.asistencia = 0
        self.vendidos = 0

        if not estadio:
            print(f"No existe un estadio con el id: {id}")
            return
        
        fila, columna = estadio.capacity

        self.asientos_Disponibles = []

        for i in range(fila):
            filas = []
            for j in range(columna):
                filas.append(True)

            self.asientos_Disponibles.append(filas)

    def mostrar_Asientos(self):
        for fila in self.asientos_Disponibles:
            strFila = ""
            for asiento in fila:
                if asiento:
                    simbolo = "+"
                else:
                    simbolo = "-"
                strFila += simbolo
            print(strFila)
            print()

    def pedir_Posicion(self):
        self.mostrar_Asientos()

        while True:
            try:
                fila = int(input("Ingrese la fila del asiento que desee: ")) - 1
                columna = int(input("Ingrese la columna del asiento que desee:  ")) - 1
                if columna < 0 or fila < 0:
                    raise Exception

                if self.asientos_Disponibles[fila][columna] == False:
                    print("El asiento que escogio ya se encuentra ocupado")
                    continue

                self.asientos_Disponibles[fila][columna] = False

                return fila, columna

            except:
                print("Ingrese unas coordenadas válidas")


    def __str__(self) -> str:
        return (f"""Id: {self.id}
Fecha: {self.date}
Equipo Local: {self.home_Team.name}
Equipo Visitante: {self.away_Team.name}""")
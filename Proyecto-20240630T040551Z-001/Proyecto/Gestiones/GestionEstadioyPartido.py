
from Clases.Equipo import Equipo
from Clases.Partido import Partido
from Clases.Estadio import Estadio
from funciones import escoger_Opcion


class GestionEstadioyPartido():
    def __init__(self, partidos: list[Partido], equipos: list[Equipo], estadios: list[Estadio]) -> None:
        self.partidos = partidos
        self.equipos = equipos
        self.estadios = estadios
        
    def start(self):
        while True:
            try:
                opcion = int(input("""1. Filtrar partidos por pais
2. Filtrar partidos por estadio
3. Filtrar partidos por fecha determinada
4. Salir"""))
                if opcion == 1:
                    self.partidos_por_pais()
                elif opcion == 2:
                    self.partidos_por_estadio()
                elif opcion == 3:
                    self.partidos_por_fecha()
                elif opcion == 4:
                    break
                else:
                    raise Exception
            except:
                print("Ingrese una opcion valida")

    def partidos_por_pais(self):
        equipo = escoger_Opcion(self.equipos)

        encontrado = False

        for partido in self.partidos:
            if partido.home_Team.id == equipo.id or partido.away_Team.id == equipo.id:
                encontrado = True
                print(partido)
                print()

        if not encontrado:
            print("No existe partidos con el equipo seleccionado")


    def partidos_por_estadio(self):
        estadio = escoger_Opcion(self.estadios)
        
        encontrado = False

        for partido in self.partidos:
            if partido.stadium_Id == estadio.id:
                encontrado = True
                print(partido)
                print()

        if not encontrado:
            print("No existen partidos con el estadio seleccionado")

    def partidos_por_fecha(self):
        fecha = self.pedirFecha()

        encontrado = False

        for partido in self.partidos:
            if partido.date == fecha:
                encontrado = True
                print(partido)
                print()

        if not encontrado:
            print("No existen partidos con dicha fecha")

    def pedirFecha(self):
        while True:
            try:
                fecha = input("Ingrese una fecha con el siguiente formato (YYYY-MM-DD): ")
                year, month, day = fecha.split("-") #["2024", "33", "14"]
                
                if len(year) < 4:
                    raise Exception
                elif len(month) < 2:
                    raise Exception
                elif len(day) < 2:
                    raise Exception
                
                yearInt = int(year)
                monthInt = int(month)
                dayInt = int(day)

                if monthInt <= 0 or monthInt > 12:
                    raise Exception
                elif dayInt <= 0 or dayInt > 31:
                    raise Exception
                return fecha
            except:
                print("Ingrese una fecha válida")

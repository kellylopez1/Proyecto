from funciones import *
class GestionEstadisticas():
    def __init__(self, clientes, estadios, partidos) -> None:
        self.clientes = clientes
        self.estadios = estadios
        self.partidos = partidos

    def start(self):
        print("""
1.	¿Cuál es el promedio de gasto de un cliente VIP en un partido (ticket + restaurante)?
2.	Mostrar tabla con la asistencia a los partidos de mejor a peor
3.	¿Cuál fue el partido con mayor asistencia?
4.	¿Cuál fue el partido con mayor boletos vendidos?
5.	Top 3 productos más vendidos en el restaurante. (Debe seleccionar el restaurante)
6.	Top 3 de clientes (clientes que más compraron boletos)
""")
        opcion = input("Ingresa el numero de la estadistica que deseas ver: ")
        while opcion not in ["1", "2", "3", "4", "5", "6"]:
            opcion = input("Ingresa el numero de la estadistica que deseas ver: ")
        if opcion == "1":
            total = 0
            vips = 0
            for cliente in self.clientes:
                if cliente.ticket.tipo ==  "VIP":
                    total += cliente.gastado
                    vips += 1
            if vips != 0:
                print(f"El promedio de gasto de los clientes VIP es de {total/vips}")
        elif opcion == "2":
            p = sorted(self.partidos, key=lambda x: x.asistencia, reverse=True)
            for partido in p:
                print(f"""{partido.home_Team.name} contra {partido.away_Team.name}
                      Estadio {partido.stadium_Id}
                      Boletos vendidos: {partido.vendidos}
                      Asistencia: {partido.asistencia}
                      """)
                if partido.vendidos != 0:
                    print(f"             Asistencia/Venta = {partido.asistencia/partido.vendidos}")
                else:
                    print(f"             Asistencia/Venta = 0")

        elif opcion == '3':
            p = sorted(self.partidos, key=lambda x: x.asistencia, reverse=True)
            print(p[0].__str__())
            print(f"CON UN TOTAL DE {p[0].asistencia} asistentes")
        elif opcion == '4':
            p = sorted(self.partidos, key=lambda x: x.vendidos, reverse=True)
            print(p[0].__str__())
            print(f"CON UN TOTAL DE {p[0].vendidos} asistentes")
        elif opcion == '5':
            estadio = escoger_Opcion(self.estadios)
            restaurante = escoger_Estadio(estadio.restaurants)
            p = sorted(restaurante.products, key=lambda x: x.vendido, reverse=True)
            for i in range(3):
                print(f"{i+1} {p[i].__str__()}")
                print(f"CON UN TOTAL DE {p[i].vendido} vendidos")
        elif opcion == "6":
            if len(self.clientes) > 2:
                p = sorted(self.clientes, key=lambda x: x.comprados, reverse=True)

                for i in range(3):
                    print(f"{i+1}{p[i].nombre} CON UN TOTAL DE {p[i].comprados} tickets comprados")
            else:
                print("No hay suficientes clientes")

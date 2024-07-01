
import requests

from Clases.Alimento import Alimento
from Clases.Bebida import Bebida
from Clases.Equipo import Equipo
from Clases.Estadio import Estadio
from Clases.Partido import Partido
from Clases.Restaurant import Restaurant
from Gestiones.GestionAsistenciaPartidos import GestionAsistenciaPartidos
from Gestiones.GestionEntradas import GestionEntradas
from Gestiones.GestionEstadioyPartido import GestionEstadioyPartido
from Gestiones.GestionEstadisticas import *
from Gestiones.GestionVentadeRestaurante import *
from Gestiones.GestionRestaurante import *

class App():
    def __init__(self) -> None:
        self.equipos = self.get_Equipos()
        self.estadios = self.get_Estadios()
        self.partidos = self.get_Partidos()
        self.clientes = []
        self.tickets = []

    def start(self):
        gestionEstadio = GestionEstadioyPartido(self.partidos, self.equipos, self.estadios)
        gestionEntradas = GestionEntradas(self.partidos, self.tickets)
        gestionAsistencia = GestionAsistenciaPartidos(self.partidos)
        gestionEstadisticas = GestionEstadisticas(self.clientes, self.estadios, self.partidos)
        gestionVenta = GestionVentadeRestaurante()
        gestionRest = GestionRestaurante(self.estadios)
        
        while True:
            #try:
                opcion = int(input("""Eurocopa Alemania 2024 \nSeleccione el módulo que desee a continuación;  
1. Gestión de Estadios y Partidos
2. Gestión de venta de entradas
3. Gestión asistencia a partidos
4. Gestión de restaurantes
5. Gestión de venta de restaurantes
6. Gestión estadísticas
7. Salir
->  """))
                if opcion == 1:
                    gestionEstadio.start()
                elif opcion == 2:
                    self.clientes.append(gestionEntradas.start())
                elif opcion == 3:    
                    gestionAsistencia.validar_Boletos(self.clientes)
                elif opcion == 4:
                    gestionRest.start()
                elif opcion == 5:
                    gestionVenta.start(self.clientes)
                elif opcion == 6:
                    gestionEstadisticas.start()
                elif opcion == 7:
                    break
                else:
                    raise Exception
            #except:
                #print("Ingrese una opción válida")

    def get_Equipos(self):
        response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json")
        data = response.json()

        equipos = []
        for equipo in data: 
            equipoNuevo = self.crear_Equipo(equipo)
            equipos.append(equipoNuevo)
            
        return equipos

    def crear_Equipo(self, equipo):
        id = equipo["id"]
        code = equipo["code"]
        name = equipo["name"]
        group = equipo["group"]

        equipoNuevo = Equipo(id, name, code, group)
        return equipoNuevo

    def get_Estadios(self):
        response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json")
        data = response.json()

        estadios = []
        for estadio in data: 
            id = estadio["id"]
            name = estadio["name"]
            city = estadio["city"]
            capacity = estadio["capacity"]
           
            restaurants = []
            for restaurant in estadio["restaurants"]:
                restaurant_Name = restaurant["name"]
               
                productos = []
                for producto in restaurant["products"]:
                    product_Name = producto["name"]  
                    product_Quantity = producto["quantity"]
                    product_Price = producto["price"]  
                    product_Stock = producto["stock"]
                    product_Aditional = producto["adicional"]
                    

                    if product_Aditional in ["alcoholic", "non-alcoholic"]:
                        bebida = Bebida(product_Name, product_Quantity, product_Price, product_Stock, product_Aditional)
                        productos.append(bebida)
                    else:
                        alimento = Alimento(product_Name, product_Quantity, product_Price, product_Stock, product_Aditional)
                        productos.append(alimento)
                        
                restaurante = Restaurant(restaurant_Name, productos)
                restaurants.append(restaurante)
            
            estadioNuevo = Estadio(id, name, city, capacity, restaurants)
            estadios.append(estadioNuevo)
            
        return estadios

    def get_Partidos(self):
        response = requests.get("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json")
        data = response.json()

        partidos = []
        for partido in data: 
            id = partido["id"]
            number = partido["number"]
            date = partido["date"]
            group = partido["group"]
            stadium_Id = partido["stadium_id"]

            home_Team =  self.crear_Equipo(partido["home"])
            away_Team = self.crear_Equipo(partido["away"])

            estadio = self.buscar_estadio_por_id(stadium_Id)

            equipoNuevo = Partido(id, number, date, group, stadium_Id, home_Team, away_Team, estadio)
            partidos.append(equipoNuevo)
            
        return partidos
    
    def buscar_estadio_por_id(self, stadiumId: str):
        for estadio in self.estadios:
            if estadio.id == stadiumId:
                return estadio
            
        return None
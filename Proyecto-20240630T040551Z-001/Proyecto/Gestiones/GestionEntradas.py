from Clases.Cliente import Cliente
from Clases.Partido import Partido
from Clases.Ticket import Ticket
from funciones import escoger_Opcion


class GestionEntradas():
    def __init__(self, partidos: list[Partido], tickets: list[Ticket]) -> None:
        self.partidos = partidos
        self.tickets = tickets

    def start(self):
        cliente = self.pedir_datos_cliente()
        partido = escoger_Opcion(self.partidos)
        tipo, costo = self.pedir_datos_tickets()
        fila, columna = partido.pedir_Posicion()
        descuento = 0
        if self.esVampiro(cliente.cedula):
            descuento += 0.5

        cantidad_Descontada = costo * descuento
        total = round(costo - cantidad_Descontada, 2)

        IVA = total * 0.16
        total += IVA
        while True:
            opcion = input("1. Para comprar, ingrese 1. Si no está seguro, ingrese 2.")

            if opcion == "1":
                break
            elif opcion =="2":
                print("Esperamos que vuelva pronto!")
                return
            else:
                print("Ingrese una opción válida")

        print(f"""Asientos: {fila + 1}, {columna +1}

Partido: {partido}

Sub total: {costo}
Cantidad descontada: {cantidad_Descontada}
IVA: {IVA}
Total: {total}
GUARDE EL ID DE SU BOLETO PARA PODER ACCEDER AL ESTADIO
""")
        
        ticket = Ticket(tipo, total, partido, [fila, columna])
        print(f"ID DEL BOLETO {ticket.id}")
        partido.vendidos +=1
        if tipo == "VIP":
            cliente.gastado += total
        cliente.comprados += 1
        self.tickets.append(ticket)
        cliente.ticket = ticket
        return cliente


    def pedir_datos_cliente(self):
        while True:
            #try:
                nombre = input("Ingrese su nombre: ")
                cedula = int(input("Ingrese su cédula: "))
                edad= int(input("Ingrese su edad: ")) 

                if not nombre.isalpha:
                    print("Inténtelo de nuevo.")
                    return (nombre)
                if len(str(cedula)) > 8:
                    print("Inténtelo de nuevo. ")
                    return (cedula)
                if len(str(edad)) > 2:
                    print("Inténtelo de nuevo.")
                    return edad
                
                cliente = Cliente(nombre, cedula, edad)
                return cliente
            #except:   
                #print("Inténtelo de nuevo.")

            #return 0

    def pedir_datos_tickets(self):
        while True:
                opcion = input("Escoja el tipo de ticket que desea (1. General 35$, 2. VIP 75$): ")

                if opcion == "1":
                    return "General", 35
                elif opcion == "2":
                    return "VIP", 75
                else:
                    print("Ingrese una opción válida")
    pass 

    def esVampiro(self, numero: int):
        return True
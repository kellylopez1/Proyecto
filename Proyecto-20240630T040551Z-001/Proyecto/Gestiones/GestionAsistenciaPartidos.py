

from Clases.Partido import Partido


class GestionAsistenciaPartidos():
    def __init__(self, partidos):
        self.partidos = partidos
        self.boletos = []
        self.boleto_Valido = []

    def validar_Boletos(self, clientes):
       boleto = input("Ingrese el codigo de su boleto: ")
       for cliente in clientes:
           if cliente.ticket.id == boleto:
                cliente.ticket.partido.asistencia += 1
                print(f"Asistencia registrada")
                return True
       return False
               
       

    def boleto_Autentico(self):
        pass


def actualizar_asistencia(codigo_boleto):
    print(f"Asistencia registrada para el boleto {codigo_boleto}")


class Requisicion:
    def __init__(self, requisicion_id, promedio, existencia_meses, cant_max, cant_solicitar, cant_recibida):
        self.requisicion_id = requisicion_id
        self.promedio = promedio
        self.existencia_meses = existencia_meses
        self.cant_max = cant_max
        self.cant_solicitar = cant_solicitar
        self.cant_recibida = cant_recibida
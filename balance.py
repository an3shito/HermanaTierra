from datetime import date

class Balance:
    def __init__(self, balance_id, saldo_anterior, entrada_nivel_sup, entregado_usuario, no_entregado, demanda_real, reajuste, saldo_sig_mes, existe_bodega):
            self.balance_id = balance_id
            self.saldo_anterior = saldo_anterior
            self.entrada_nivel_sup = entrada_nivel_sup
            self.entregado_usuario = entregado_usuario
            self.no_entregado = no_entregado
            self.demanda_real = demanda_real
            self.reajuste = reajuste
            self.saldo_sig_mes = saldo_sig_mes
            self.existe_bodega = existe_bodega
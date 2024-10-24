class Bus:
    """
    Classe que representa um barramento em um sistema de potência.

    Atributos:
    ----------
    bus_i : int
        Identificador único do barramento.
    bus_type : int
        Tipo do barramento (1 = PQ, 2 = PV, 3 = Slack).
    Pd : float
        Potência ativa demandada no barramento (em MW).
    Qd : float
        Potência reativa demandada no barramento (em MVAr).
    Gs : float
        Condutância de shunt conectada ao barramento (em p.u.).
    Bs : float
        Susceptância de shunt conectada ao barramento (em p.u.).
    area : int
        Área a que o barramento pertence (usada para agrupamento).
    Vm : float
        Magnitude da tensão no barramento (em p.u.).
    Va : float
        Ângulo da tensão no barramento (em graus).
    baseKV : float
        Nível de tensão base do barramento (em kV).
    zone : int
        Zona a que o barramento pertence (usada para análises específicas).
    Vmax : float
        Tensão máxima permitida no barramento (em p.u.).
    Vmin : float
        Tensão mínima permitida no barramento (em p.u.).

    Métodos:
    --------
    __str__():
        Retorna uma string com todos os atributos do barramento formatados e separados por tabulação.
    """

    def __init__(self, bus_i, bus_type, Pd, Qd, Gs, Bs, area, Vm, Va, baseKV, zone, Vmax, Vmin):
        self.bus_i = bus_i
        self.type = bus_type
        self.Pd = Pd
        self.Qd = Qd
        self.Gs = Gs
        self.Bs = Bs
        self.area = area
        self.Vm = Vm
        self.Va = Va
        self.baseKV = baseKV
        self.zone = zone
        self.Vmax = Vmax
        self.Vmin = Vmin

    def __str__(self):
        return "\t".join(map(str, [
            self.bus_i, self.type, self.Pd, self.Qd, self.Gs, self.Bs, self.area,
            self.Vm, self.Va, self.baseKV, self.zone, self.Vmax, self.Vmin
        ]))
    


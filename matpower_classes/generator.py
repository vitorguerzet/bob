class Generator:
    """
    Classe que representa um gerador em um sistema de potência.

    Atributos:
    ----------
    bus : int
        Identificador do barramento ao qual o gerador está conectado.
    Pg : float
        Potência ativa gerada pelo gerador (em MW).
    Qg : float
        Potência reativa gerada pelo gerador (em MVAr).
    Qmax : float
        Limite máximo de potência reativa que o gerador pode fornecer (em MVAr).
    Qmin : float
        Limite mínimo de potência reativa que o gerador pode fornecer (em MVAr).
    Vg : float
        Tensão de operação no barramento de conexão do gerador (em p.u.).
    mBase : float
        Base de potência para o gerador (em MVA).
    status : int
        Status do gerador: 1 para ativo, 0 para inativo.
    Pmax : float
        Potência ativa máxima que o gerador pode fornecer (em MW).
    Pmin : float
        Potência ativa mínima que o gerador pode fornecer (em MW).
    Pc1 : float, opcional
        Ponto de custo de peça linear 1. Usado em curvas de custo do gerador (opcional).
    Pc2 : float, opcional
        Ponto de custo de peça linear 2. Usado em curvas de custo do gerador (opcional).
    Qc1min : float, opcional
        Limite mínimo de potência reativa no ponto 1 da curva de custo (opcional).
    Qc1max : float, opcional
        Limite máximo de potência reativa no ponto 1 da curva de custo (opcional).
    Qc2min : float, opcional
        Limite mínimo de potência reativa no ponto 2 da curva de custo (opcional).
    Qc2max : float, opcional
        Limite máximo de potência reativa no ponto 2 da curva de custo (opcional).
    ramp_agc : float, opcional
        Taxa de rampa para controle automático de geração (AGC), em MW/min.
    ramp_10 : float, opcional
        Taxa de rampa para aumento de 10 minutos, em MW.
    ramp_30 : float, opcional
        Taxa de rampa para aumento de 30 minutos, em MW.
    ramp_q : float, opcional
        Taxa de rampa para ajuste de potência reativa, em MVAr/min.
    apf : float, opcional
        Fator de participação no controle de área de potência (Area Participation Factor).

    Métodos:
    --------
    __str__():
        Retorna uma string formatada com todos os atributos do gerador, separados por tabulação.
    """
    
    def __init__(self, bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1=0, Pc2=0, Qc1min=0, Qc1max=0, Qc2min=0, Qc2max=0, ramp_agc=0, ramp_10=0, ramp_30=0, ramp_q=0, apf=0):
        self.bus = bus
        self.Pg = Pg
        self.Qg = Qg
        self.Qmax = Qmax
        self.Qmin = Qmin
        self.Vg = Vg
        self.mBase = mBase
        self.status = status
        self.Pmax = Pmax
        self.Pmin = Pmin
        self.Pc1 = Pc1
        self.Pc2 = Pc2
        self.Qc1min = Qc1min
        self.Qc1max = Qc1max
        self.Qc2min = Qc2min
        self.Qc2max = Qc2max
        self.ramp_agc = ramp_agc
        self.ramp_10 = ramp_10
        self.ramp_30 = ramp_30
        self.ramp_q = ramp_q
        self.apf = apf

    def __str__(self):
        return "\t".join(map(str, [
            self.bus, self.Pg, self.Qg, self.Qmax, self.Qmin, self.Vg, self.mBase,
            self.status, self.Pmax, self.Pmin, self.Pc1, self.Pc2, self.Qc1min, self.Qc1max,
            self.Qc2min, self.Qc2max, self.ramp_agc, self.ramp_10, self.ramp_30, self.ramp_q, self.apf
        ]))

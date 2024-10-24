class Transformer:
    """
    Classe que representa um transformador (modelo específico de Branch) em um sistema de potência.

    Atributos:
    ----------
    fbus : int
        Identificador do barramento de origem (lado de alta tensão).
    tbus : int
        Identificador do barramento de destino (lado de baixa tensão).
    r : float
        Resistência série do transformador (em p.u.).
    x : float
        Reatância série do transformador (em p.u.).
    b : float
        Susceptância shunt do transformador (em p.u.).
    rateA : float
        Capacidade nominal contínua do transformador (em MVA).
    rateB : float
        Capacidade nominal contínua do transformador (em MVA).
    rateC : float
        Capacidade nominal contínua do transformador (em MVA).
    tap : float
        Relação de transformação (tap ratio) do transformador. Ajusta a tensão entre os lados primário e secundário.
    angle : float
        Deslocamento de fase introduzido pelo transformador (em graus). Usado para modelar transformadores que introduzem um desvio de fase, como transformadores Delta-Y.
    status : int
        Status do transformador: 1 para ativo, 0 para inativo.
    angmin : float
        Limite inferior do ângulo de deflexão permitido no transformador (em graus).
    angmax : float
        Limite superior do ângulo de deflexão permitido no transformador (em graus).

    Métodos:
    --------
    __str__():
        Retorna uma string formatada com todos os atributos do transformador, separados por tabulação.
    """
    
    def __init__(self, fbus, tbus, r, x, b, rate, ratio, angle, status, angmin, angmax):
        self.fbus = fbus
        self.tbus = tbus
        self.r = r
        self.x = x
        self.b = b
        self.rateA = rate
        self.rateB = rate
        self.rateC = rate
        self.tap = ratio
        self.angle = angle
        self.status = status
        self.angmin = angmin
        self.angmax = angmax

    def __str__(self):
        return "\t".join(map(str, [
            self.fbus, self.tbus, self.r, self.x, self.b, self.rateA, self.rateB,
            self.rateC, self.tap, self.angle, self.status, self.angmin, self.angmax
        ]))

class Branch:
    """
    Classe que representa uma linha de transmissão ou transformador em um sistema de potência.

    Atributos:
    ----------
    fbus : int
        Identificador do barramento de origem (de onde a linha de transmissão ou transformador parte).
    tbus : int
        Identificador do barramento de destino (para onde a linha de transmissão ou transformador vai).
    r : float
        Resistência série da linha de transmissão ou transformador (em p.u.).
    x : float
        Reatância série da linha de transmissão ou transformador (em p.u.).
    b : float
        Susceptância shunt da linha de transmissão ou transformador (em p.u.).
    rateA : float
        Capacidade nominal contínua da linha ou transformador (em MVA).
    rateB : float
        Capacidade nominal por curto período da linha ou transformador (em MVA).
    rateC : float
        Capacidade nominal sob condições extremas da linha ou transformador (em MVA).
    ratio : float
        Relação de transformação do transformador (tap ratio), usado para ajustar a tensão no lado de alta tensão. Um valor de 1.0 indica uma relação 1:1.
    angle : float
        Deslocamento de fase introduzido pelo transformador (em graus). Usado para modelar transformadores que introduzem um desvio de fase (ex: transformadores Delta-Y).
    status : int
        Status do ramo: 1 para ramo ativo, 0 para ramo desativado.
    angmin : float
        Limite inferior do ângulo de deflexão permitida na linha de transmissão ou transformador (em graus).
    angmax : float
        Limite superior do ângulo de deflexão permitida na linha de transmissão ou transformador (em graus).

    Métodos:
    --------
    __str__():
        Retorna uma string formatada com todos os atributos do ramo, separados por tabulação.
    """
    
    def __init__(self, fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax):
        self.fbus = fbus
        self.tbus = tbus
        self.r = r
        self.x = x
        self.b = b
        self.rateA = rateA
        self.rateB = rateB
        self.rateC = rateC
        self.ratio = ratio
        self.angle = angle
        self.status = status
        self.angmin = angmin
        self.angmax = angmax

    def __str__(self):
        return "\t".join(map(str, [
            self.fbus, self.tbus, self.r, self.x, self.b, self.rateA, self.rateB,
            self.rateC, self.ratio, self.angle, self.status, self.angmin, self.angmax
        ]))

class GeneratorCost:
    """
    Classe que representa a função de custo de um gerador em um sistema de potência.

    Atributos:
    ----------
    model : int
        Tipo de modelo de custo (1 = peça linear, 2 = polinomial).
    startup : float
        Custo de inicialização do gerador (em unidades monetárias).
    shutdown : float
        Custo de desligamento do gerador (em unidades monetárias).
    n : int
        Número de termos na função de custo (incluindo o termo constante).
    coefficients : tuple
        Coeficientes da função de custo. Para modelo peça linear, são os pontos da curva
        (Pc1, Pc2, ...). Para modelo polinomial, são os coeficientes do polinômio
        (c_n-1, c_n-2, ..., c_0).

    Métodos:
    --------
    __str__():
        Retorna uma string formatada com todos os atributos da função de custo, separados por tabulação.
    """
    
    def __init__(self, model, startup, shutdown, n, *coefficients):
        self.model = model
        self.startup = startup
        self.shutdown = shutdown
        self.n = n
        self.coefficients = coefficients

    def __str__(self):
        return "\t".join(map(str, [
            self.model, self.startup, self.shutdown, self.n, *self.coefficients
        ]))

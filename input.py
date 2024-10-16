import unittest
from matpower_classes import Bus, Generator, Branch, Transformer, GeneratorCost, MatpowerCase

#n_buses=input('quantos barramentos?\n')
#n_lines=input('quantas linhas de transmissão?\n')
buses=[]
branches=[]
generators=[]
transformers=[]
gencosts=[]
i=True
while i:
    comp = input('qual componente deseja acrescentar na sumilação: bus=1, generator=2, branch=3, transformer=4, gencost=5\n verificar=6, gerar arquivo.m e encerra=7 \n')

    match comp:
        case '1':
        
            bus_i=float(input('Identificador único do barramento\n'))
            bus_type=float(input('Tipo do barramento (1 = PQ, 2 = PV, 3 = Slack)\n'))
            Pd=float(input('Potência ativa demandada no barramento (em MW)\n'))
            Qd=float(input('Potência reativa demandada no barramento (em MVAr)\n'))
            Gs=float(input('Condutância de shunt conectada ao barramento (em p.u.)\n'))
            Bs=float(input('Susceptância de shunt conectada ao barramento (em p.u.)\n'))
            area=float(input('Área a que o barramento pertence (usada para agrupamento)\n'))
            Vm=float(input('Magnitude da tensão no barramento (em p.u.)\n'))
            Va=float(input('Ângulo da tensão no barramento (em graus)\n'))
            baseKV=float(input('Nível de tensão base do barramento (em kV)\n'))
            zone=float(input('Zona a que o barramento pertence (usada para análises específicas)\n'))
            Vmax=float(input('Tensão máxima permitida no barramento (em p.u.)\n'))
            Vmin=float(input('Tensão mínima permitida no barramento (em p.u.)\n'))

            #(self, bus_i, bus_type, Pd, Qd, Gs, Bs, area, Vm, Va, baseKV, zone, Vmax, Vmin)
            buses.append(Bus(bus_i, bus_type, Pd, Qd, Gs, Bs, area, Vm, Va, baseKV, zone, Vmax, Vmin))
            
            

        case '2':

            bus=float(input('Identificador do barramento ao qual o gerador está conectado\n'))
            Pg=float(input('Potência ativa gerada pelo gerador (em MW)\n'))
            Qg=float(input('Potência reativa gerada pelo gerador (em MVAr)\n'))
            Qmax=float(input('Limite máximo de potência reativa que o gerador pode fornecer (em MVAr)\n'))
            Qmin=float(input('Limite mínimo de potência reativa que o gerador pode fornecer (em MVAr)\n'))
            Vg=float(input('Tensão de operação no barramento de conexão do gerador (em p.u.)\n'))
            mBase=float(input('Base de potência para o gerador (em MVA)\n'))
            status=float(input('Status do gerador: 1 para ativo, 0 para inativo\n'))
            Pmax=float(input('Potência ativa máxima que o gerador pode fornecer (em MW)\n'))
            Pmin=float(input('Potência ativa mínima que o gerador pode fornecer (em MW)\n'))

            #(self, bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1=0, Pc2=0, Qc1min=0, Qc1max=0, Qc2min=0, Qc2max=0, ramp_agc=0, ramp_10=0, ramp_30=0, ramp_q=0, apf=0):
            generators.append(Generator(bus ,Pg, Qg, Qmax, Qmin, Vg, mBase, status,  Pmax, Pmin))
        case '3':

            fbus=float(input('Identificador do barramento de origem (de onde a linha de transmissão ou transformador parte)\n'))
            tbus=float(input('Identificador do barramento de destino (para onde a linha de transmissão ou transformador vai)\n'))
            r=float(input('Resistência série da linha de transmissão ou transformador (em p.u.)\n'))
            x=float(input('Reatância série da linha de transmissão ou transformador (em p.u.)\n'))
            b=float(input('Susceptância shunt da linha de transmissão ou transformador (em p.u.)\n'))
            rateA=float(input('Capacidade nominal contínua da linha ou transformador (em MVA)\n'))
            rateB=float(input('Capacidade nominal por curto período da linha ou transformador (em MVA)\n'))
            rateC=float(input('Capacidade nominal sob condições extremas da linha ou transformador (em MVA)\n'))
            ratio=float(input('Relação de transformação do transformador (tap ratio), usado para ajustar a tensão no lado de alta tensão. Um valor de 1.0 indica uma relação 1:1\n'))
            angle=float(input('Deslocamento de fase introduzido pelo transformador (em graus). Usado para modelar transformadores que introduzem um desvio de fase (ex: transformadores Delta-Y)\n'))
            status=float(input('Status do ramo: 1 para ramo ativo, 0 para ramo desativado\n'))
            angmin=float(input('Limite inferior do ângulo de deflexão permitida na linha de transmissão ou transformador (em graus)\n'))
            angmax=float(input('Limite superior do ângulo de deflexão permitida na linha de transmissão ou transformador (em graus)\n'))

            branches.append(Branch(fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax))
            #(self, fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax)
    
        case '4':

            fbus=float(input('Identificador do barramento de origem (de onde a linha de transmissão ou transformador parte)\n'))
            tbus=float(input('Identificador do barramento de destino (para onde a linha de transmissão ou transformador vai)\n'))
            r=float(input('Resistência série da linha de transmissão ou transformador (em p.u.)\n'))
            x=float(input('Reatância série da linha de transmissão ou transformador (em p.u.)\n'))
            b=float(input('Susceptância shunt da linha de transmissão ou transformador (em p.u.)\n'))
            rate=float(input('Capacidade nominal contínua do transformador (em MVA)\n'))
            ratio=float(input('Relação de transformação do transformador (tap ratio), usado para ajustar a tensão no lado de alta tensão. Um valor de 1.0 indica uma relação 1:1\n'))
            angle=float(input('Deslocamento de fase introduzido pelo transformador (em graus). Usado para modelar transformadores que introduzem um desvio de fase (ex: transformadores Delta-Y)\n'))
            status=float(input('Status do ramo: 1 para ramo ativo, 0 para ramo desativado\n'))
            angmin=float(input('Limite inferior do ângulo de deflexão permitida na linha de transmissão ou transformador (em graus)\n'))
            angmax=float(input('Limite superior do ângulo de deflexão permitida na linha de transmissão ou transformador (em graus)\n'))
            
            transformers.append(Transformer(fbus, tbus, r, x, b, rate, ratio, angle, status, angmin, angmax))
            #(self, fbus, tbus, r, x, b, rate, ratio, angle, status, angmin, angmax):
        case '5':
            model=float(input('Tipo de modelo de custo (1 = peça linear, 2 = polinomial)\n'))
            startup=float(input('Custo de inicialização do gerador (em unidades monetárias)\n'))
            shutdown=float(input('Custo de desligamento do gerador (em unidades monetárias)\n'))
            n=float(input('Número de termos na função de custo (incluindo o termo constante)\n'))
            coefficients=float(input('Coeficientes da função de custo. Para modelo peça linear, são os pontos da curva (Pc1, Pc2, ...). Para modelo polinomial, são os coeficientes do polinômio (c_n-1, c_n-2, ..., c_0)\n'))

        #(self, model, startup, shutdown, n, *coefficients)
            gencosts.append(GeneratorCost(2, 0, 0, 3, 0.02, 2.0, 0))  
        case '6':
            print(buses)
            print(branches)
            print(generators)
            print(transformers)
            print(gencosts)     
        case _:
            matpower_case = MatpowerCase(case_name='case_custom')

            for bus in buses:
                matpower_case.add_bus(bus)

            for generator in generators:
                matpower_case.add_generator(generator)

            for branch in branches:
                matpower_case.add_branch(branch)

            for trasnf in transformers:
                matpower_case.add_transformer(trasnf)

            for cost in gencosts:
                matpower_case.add_gencost(cost)

            matpower_case.save_case_file(filename=input('nome do arquivo:') + '.m')
            i=False





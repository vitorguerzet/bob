from matpower_classes import Bus, Generator, Branch, Transformer, GeneratorCost, MatpowerCase

def create_case_example():
    matpower_case = MatpowerCase(case_name='case_custom')

    # Adicionar barramentos
    buses = [
        Bus(1, 3, 0, 0, 0, 0, 1, 1, 0, 230, 1, 1.1, 0.94),
        Bus(2, 1, 0, 0, 0, 0, 1, 1.045, 0, 230, 1, 1.06, 0.94),
        Bus(3, 2, 5, 0, 0, 0, 1, 1.01, 0, 13.8, 1, 1.06, 0.94)
    ]

        
    for bus in buses:
        matpower_case.add_bus(bus)

    # Adicionar geradores
    generators = [
        Generator(1, 10, 0, 30, -30, 1.06, 100, 1, 10, 0),
        Generator(2, 10, 0, 30, -30, 1.045, 100, 1, 10, 0)
    ]

    for generator in generators:
        matpower_case.add_generator(generator)

    # Adicionar ramos
    branches = [
        Branch(1, 2, 0.017,	0.092, 0.158, 250, 250, 250, 0, 0, 1, -360, 360)
    ]

    for branch in branches:
        matpower_case.add_branch(branch)

    transformers = [
        Transformer(2, 3, 0.01, 0.003, 0.0002, 100, 16.67, -30, 1, -360, 360)
    ]
    
    for trasnf in transformers:
        matpower_case.add_transformer(trasnf)
        
    # Adicionar custos dos geradores
    gencosts = [
        GeneratorCost(2, 0, 0, 3, 0.02, 2.0, 0),
        GeneratorCost(2, 0, 0, 3, 0.0175, 1.75, 0)
    ]

    for cost in gencosts:
        matpower_case.add_gencost(cost)

    # Salvar arquivo de caso MATPOWER
    matpower_case.save_case_file(filename='case_custom.m')

def create_case_ieee4bus():
    matpower_case = MatpowerCase(case_name='case_ieee4bus')

    # Adicionar barramentos
    buses = [
        Bus(1, 3, 0, 0, 0, 0, 1, 1.06, 0, 230, 1, 1.06, 0.94),  # Slack bus
        Bus(2, 1, 20, 10, 0, 0, 1, 1.045, 0, 230, 1, 1.06, 0.94), # PQ bus
        Bus(3, 1, 45, 15, 0, 0, 1, 1.01, 0, 230, 1, 1.06, 0.94),  # PQ bus
        Bus(4, 2, 40, 5, 0, 0, 1, 1.05, 0, 230, 1, 1.06, 0.94)    # PV bus
    ]

    for bus in buses:
        matpower_case.add_bus(bus)

    # Adicionar geradores
    generators = [
        Generator(1, 50, 0, 100, -100, 1.06, 100, 1, 250, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        Generator(4, 40, 0, 100, -100, 1.05, 100, 1, 250, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ]

    for generator in generators:
        matpower_case.add_generator(generator)

    # Adicionar ramos
    branches = [
        Branch(1, 2, 0.02, 0.04, 0.03, 130, 130, 130, 0, 0, 1, -360, 360),
        Branch(2, 3, 0.05, 0.2, 0.04, 130, 130, 130, 0, 0, 1, -360, 360),
        Branch(3, 4, 0.08, 0.3, 0.05, 130, 130, 130, 0, 0, 1, -360, 360),
        Branch(4, 1, 0.1, 0.4, 0.06, 130, 130, 130, 0, 0, 1, -360, 360)
    ]

    for branch in branches:
        matpower_case.add_branch(branch)

    # Adicionar custos dos geradores
    gencosts = [
        GeneratorCost(2, 0, 0, 3, 0.02, 2.0, 0),
        GeneratorCost(2, 0, 0, 3, 0.0175, 1.75, 0)
    ]

    for cost in gencosts:
        matpower_case.add_gencost(cost)

    # Salvar arquivo de caso MATPOWER
    matpower_case.save_case_file(filename='case_ieee4bus.m')
    
if __name__ == "__main__":
    create_case_example()

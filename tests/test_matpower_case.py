import unittest
from matpower_classes import Bus, Generator, Branch, GeneratorCost, MatpowerCase

class TestMatpowerCase(unittest.TestCase):
    def test_case_creation(self):
        matpower_case = MatpowerCase()

        # Adicionar barramentos
        buses = [
            Bus(1, 3, 0, 0, 0, 0, 1, 1.06, 0, 230, 1, 1.06, 0.94),
            Bus(2, 1, 20, 10, 0, 0, 1, 1.045, -5, 230, 1, 1.06, 0.94),
            Bus(3, 1, 45, 15, 0, 0, 1, 1.01, -10, 230, 1, 1.06, 0.94)
        ]

        for bus in buses:
            matpower_case.add_bus(bus)

        # Adicionar geradores
        generators = [
            Generator(1, 50, 0, 30, -30, 1.06, 100, 1, 50, 10),
            Generator(2, 20, 0, 30, -30, 1.045, 100, 1, 20, 10)
        ]

        for generator in generators:
            matpower_case.add_generator(generator)

        # Adicionar ramos
        branches = [
            Branch(1, 2, 0.02, 0.06, 0.03, 130, 130, 130, 0, 0, 1, -360, 360),
            Branch(1, 3, 0.08, 0.24, 0.025, 130, 130, 130, 0, 0, 1, -360, 360),
            Branch(2, 3, 0.06, 0.18, 0.02, 65, 65, 65, 0, 0, 1, -360, 360)
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

        case_data = matpower_case.generate_case()
        self.assertIn("mpc.bus", case_data)
        self.assertIn("mpc.gen", case_data)
        self.assertIn("mpc.branch", case_data)
        self.assertIn("mpc.gencost", case_data)

if __name__ == '__main__':
    unittest.main()

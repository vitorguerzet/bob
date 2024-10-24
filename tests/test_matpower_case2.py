import unittest
from matpower_classes import Bus, Generator, Branch, GeneratorCost, MatpowerCase

class TestMatpowerCase(unittest.TestCase):

    def setUp(self):
        self.case = MatpowerCase(version=2, baseMVA=100)

    def test_add_bus(self):
        self.case.add_bus(Bus(1, 1, 100, 50, 0, 0, 1, 1.06, 0, 230, 1, 1.06, 0.94))
        self.assertEqual(len(self.case.buses), 1)
        self.assertEqual(self.case.buses[0].Pd, 100)

    def test_generate_case(self):
        self.case.add_bus(Bus(1, 1, 100, 50, 0, 0, 1, 1.06, 0, 230, 1, 1.06, 0.94))
        self.case.add_generator(Generator(1, 50, 0, 100, -100, 1.06, 100, 1, 250, 10))
        self.case.add_branch(Branch(1, 2, 0.01, 0.03, 0.02, 100, 100, 100, 0, 0, 1, -360, 360))
        case_data = self.case.generate_case()
        self.assertIn('mpc.bus', case_data)
        self.assertIn('mpc.gen', case_data)
        self.assertIn('mpc.branch', case_data)

if __name__ == '__main__':
    unittest.main()

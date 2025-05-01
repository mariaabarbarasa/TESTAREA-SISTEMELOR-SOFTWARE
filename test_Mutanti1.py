import unittest
from ModuloGCD import ModuloGCD

class ModuloGCDTest(unittest.TestCase):
    def test_valid_inputs(self):
        self.assertEqual(ModuloGCD(10, 5, 3).cmmdc(), 2)
        self.assertEqual(ModuloGCD(15, 10, 4).cmmdc(), 1)
        self.assertEqual(ModuloGCD(8, 12, 5).cmmdc(), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-5, 5, 2).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(50, '5', 4).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(5, -5, -2).cmmdc()

    def test_boundary_values(self):
        self.assertEqual(ModuloGCD(1, 10, 3).cmmdc(), 1)
        self.assertEqual(ModuloGCD(21, 1, 5).cmmdc(), 1)
        self.assertEqual(ModuloGCD(33, 11, 1).cmmdc(), 0)
        self.assertEqual(ModuloGCD(15, 3, 2).cmmdc(), 1)

    def test_instruction_coverage(self):
        self.assertEqual(ModuloGCD(43, 17, 2).cmmdc(), 1)

    def test_decision_coverage(self):
        self.assertEqual(ModuloGCD(14, 10, 5).cmmdc(), 2)

    def test_condition_coverage(self):
        with self.assertRaises(ValueError):
            ModuloGCD('9', 4, 3).cmmdc()
        self.assertEqual(ModuloGCD(4, 1, 5).cmmdc(), 1)

    def test_independent_paths(self):
        with self.assertRaises(ValueError):
            ModuloGCD('10', 3, 6).cmmdc()
        self.assertEqual(ModuloGCD(55, 10, 12).cmmdc(), 5)

if __name__ == '__main__':
    unittest.main()

import unittest
from ModuloGCD import ModuloGCD

import unittest

class ModuloGCDTest(unittest.TestCase):
    """1) Partitionare de echivalenta"""
    
    def test_equivalence_partitioning(self):
        with self.subTest("G111 - Valid inputs"):
            result=ModuloGCD(10, 5, 2).cmmdc()
            self.assertEqual(result, 1)

        invalid_cases=[
            ("G211 - Invalid a", -5, 5, 2),
            ("G121 - Invalid b", 50, "5", 4),
            ("G112 - Invalid c", 43, 5, -2),
            ("G122 - Invalid b and c", 5, -5, -2),
            ("G212 - Invalid a and c", 100.2, 31, None),
            ("G221 - Invalid a and b", -5, 32.2, 6),
            ("G222 - Invalid a, b, and c", -5, 15.2, "12"),
        ]
        
        for name, a, b, c in invalid_cases:
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    ModuloGCD(a, b, c).cmmdc()

            
    """2) Analiza valorilor de frontiera"""
    
    def test_boundary_value_analysis(self):
        error_cases=[
            ("a = 0", 0, 5, 2),
            ("b = 0", 7, 0, 3),
            ("c = 0", 7, 21, 0),
        ]
        
        for name, a, b, c in error_cases:
            with self.subTest(f"Error case: {name}"):
                with self.assertRaises(ValueError):
                    ModuloGCD(a, b, c).cmmdc()

        valid_cases=[
            ("a = 1", 1, 10, 3, 1),
            ("a = 2", 2, 5, 2, 1),
            ("b = 1", 21, 1, 5, 1),
            ("b = 2", 14, 2, 7, 2),
            ("c = 1", 33, 11, 1, 0),
            ("c = 2", 15, 3, 2, 1),
        ]

        for name, a, b, c, expected in valid_cases:
            with self.subTest(f"Valid case: {name}"):
                result = ModuloGCD(a, b, c).cmmdc()
                self.assertEqual(result, expected)
    
    """3) Acoperire la nivel de instructiune"""
    
    def test_statement_coverage(self):
        statement_cases = [
            ("Statement coverage 1", 43, 17, 2, 1),
            ("Statement coverage 2", 7, 19, 3, 1),
        ]
        
        for name, a, b, c, expected in statement_cases:
            with self.subTest(name):
                result = ModuloGCD(a, b, c).cmmdc()
                self.assertEqual(result, expected)
        
    """4) Acoperire la nivel de decizie"""
    
    def test_decision_coverage(self):
        decision_valid_cases=[
            ("Loop skipped", 10, 10, 12, 10),
            ("Loop true branch", 14, 10, 5, 2),
        ]
        
        for name, a, b, c, expected in decision_valid_cases:
            with self.subTest(f"Decision: {name}"):
                result = ModuloGCD(a, b, c).cmmdc()
                self.assertEqual(result, expected)
        
        with self.subTest("Decision: Invalid input"):
            with self.assertRaises(ValueError):
                ModuloGCD("10", 5, 2).cmmdc()
        
    """5) Acoperire la nivel de conditie"""
    
    def test_condition_coverage(self):
        condition_error_cases=[
            ("Condition - isinstance fail", "9", 4, 3),
            ("Condition - value check fail", 10, -2, 3),
        ]
        
        for name, a, b, c in condition_error_cases:
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    ModuloGCD(a, b, c).cmmdc()

        condition_valid_cases=[
            ("While condition true", 4, 6, 6, 2),
            ("While condition false", 3, 3, 6, 3),
            ("If condition true", 4, 1, 5, 1),
            ("If condition false", 1, 3, 10, 1),
        ]
        
        for name, a, b, c, expected in condition_valid_cases:
            with self.subTest(name):
                result = ModuloGCD(a, b, c).cmmdc()
                self.assertEqual(result, expected)
        
    """6) Testarea circuitelor independente"""
    
    def test_independent_paths_coverage(self):
        error_paths=[
            ("Exit on isinstance failure", "10", 3, 6),
            ("Exit on value check failure", 10, 3.3, 6),
            ("Exit on both checks failing", "10", 3.3, 6),
        ]
        
        for name, a, b, c in error_paths:
            with self.subTest(name):
                with self.assertRaises(ValueError):
                    ModuloGCD(a, b, c).cmmdc()
        
        valid_paths=[
            ("Exit when a == b", 10, 10, 12, 10),
            ("Loop executed", 55, 10, 12, 5),
        ]
        
        for name, a, b, c, expected in valid_paths:
            with self.subTest(name):
                result = ModuloGCD(a, b, c).cmmdc()
                self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()

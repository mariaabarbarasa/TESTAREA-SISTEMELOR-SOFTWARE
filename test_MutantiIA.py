import unittest
from ModuloGCD import ModuloGCD

class TestModuloGCDECP(unittest.TestCase):
    
    """Partitionare in clase de echivalenta"""

    # Valid input: distinct positive integers
    def test_valid_distinct_inputs(self):
        m = ModuloGCD(48, 18, 7)
        self.assertEqual(m.cmmdc(), 6 % 7)  # GCD(48,18)=6

    # Valid input: a == b
    def test_valid_equal_inputs(self):
        m = ModuloGCD(20, 20, 6)
        self.assertEqual(m.cmmdc(), 20 % 6)  # Direct return

    # Invalid input: non-integer values
    def test_non_integer_input(self):
        with self.assertRaises(ValueError):
            ModuloGCD(10.5, 5, 3).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD("10", 5, 3).cmmdc()

    # Invalid input: zero or negative numbers
    def test_zero_or_negative_input(self):
        with self.assertRaises(ValueError):
            ModuloGCD(0, 10, 5).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(-10, 20, 5).cmmdc()

    # Invalid input: c <= 0 (modulo must be positive)
    def test_invalid_modulo(self):
        with self.assertRaises(ValueError):
            ModuloGCD(15, 10, 0).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(15, 10, -3).cmmdc()
            
    """Analiza valorilor de frontiera"""
            
    # Valid minimum boundary values
    def test_min_valid_values(self):
        m = ModuloGCD(1, 1, 1)
        self.assertEqual(m.cmmdc(), 1 % 1)  # 1 % 1 = 0

    # a = 1, b just above 1
    def test_a_one_b_two(self):
        m = ModuloGCD(1, 2, 5)
        self.assertEqual(m.cmmdc(), 1 % 5)  # GCD(1,2)=1

    # Edge: max allowed iterations hit (simulate infinite loop)
    def test_potential_infinite_loop(self):
        with self.assertRaises(RuntimeError):
            # Constructing inputs that alternate without reducing quickly
            m = ModuloGCD(999_999, 1, 3)
            m.cmmdc()

    # Invalid: zero values (lower than minimum valid boundary)
    def test_zero_input(self):
        with self.assertRaises(ValueError):
            ModuloGCD(0, 5, 3).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(5, 0, 3).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(5, 3, 0).cmmdc()

    # Invalid: negative values
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-1, 5, 2).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(5, -1, 2).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(5, 2, -1).cmmdc()
            
    """Acoperire la nivel de instructiune"""        
        
    def test_valid_shortcut_equal_values(self):
        # Covers the: if a == b: return a % c
        m = ModuloGCD(12, 12, 5)
        self.assertEqual(m.cmmdc(), 12 % 5)

    def test_valid_distinct_values(self):
        # Covers full while loop (a > b and b > a cases)
        m = ModuloGCD(9, 6, 4)  # GCD(9,6)=3
        self.assertEqual(m.cmmdc(), 3 % 4)

    def test_valid_reverse_order(self):
        # Covers loop path where a < b initially
        m = ModuloGCD(6, 9, 5)  # GCD(6,9)=3
        self.assertEqual(m.cmmdc(), 3 % 5)

    def test_invalid_a_type(self):
        # Triggers validate_integer type check
        with self.assertRaises(ValueError):
            ModuloGCD("10", 5, 3).cmmdc()

    def test_invalid_b_value(self):
        # Triggers validate_integer value <= 0
        with self.assertRaises(ValueError):
            ModuloGCD(10, 0, 3).cmmdc()

    def test_invalid_c_value(self):
        # Covers: if c <= 0: raise ValueError
        with self.assertRaises(ValueError):
            ModuloGCD(10, 5, -1).cmmdc()

    def test_loop_max_iterations_exceeded(self):
        # Forces too many iterations -> RuntimeError
        with self.assertRaises(RuntimeError):
            ModuloGCD(10**6, 1, 3).cmmdc()
            
            
    """Acoperire la nivel de conditie"""
    
    # 1. validate_integer: isinstance is False
    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            ModuloGCD("5", 3, 2).cmmdc()

    # 2. validate_integer: value <= 0
    def test_invalid_value_zero(self):
        with self.assertRaises(ValueError):
            ModuloGCD(0, 3, 2).cmmdc()

    # 3. c <= 0
    def test_invalid_modulo(self):
        with self.assertRaises(ValueError):
            ModuloGCD(10, 5, -1).cmmdc()

    # 4. a == b → True (shortcut path)
    def test_equal_values(self):
        m = ModuloGCD(12, 12, 7)
        self.assertEqual(m.cmmdc(), 12 % 7)

    # 5. a != b → True (loop runs)
    def test_distinct_values(self):
        m = ModuloGCD(8, 5, 3)  # GCD=1
        self.assertEqual(m.cmmdc(), 1 % 3)

    # 6. a > b inside loop
    def test_a_greater_than_b(self):
        m = ModuloGCD(20, 5, 6)
        self.assertEqual(m.cmmdc(), 5 % 6)

    # 7. a < b inside loop
    def test_a_less_than_b(self):
        m = ModuloGCD(6, 9, 5)
        self.assertEqual(m.cmmdc(), 3 % 5)

    # 8. iterations > max_iterations
    def test_max_iterations_exceeded(self):
        with self.assertRaises(RuntimeError):
            ModuloGCD(10**6, 1, 3).cmmdc()
            
    """Testarea circuitelor independente"""
    
    # Path 1: All valid, a == b → returns a % c without loop
    def test_path_equal_values(self):
        m = ModuloGCD(10, 10, 4)
        self.assertEqual(m.cmmdc(), 10 % 4)

    # Path 2: Loop runs, a > b on first iteration
    def test_path_a_greater_than_b(self):
        m = ModuloGCD(15, 5, 6)  # GCD = 5
        self.assertEqual(m.cmmdc(), 5 % 6)

    # Path 3: Loop runs, a < b on first iteration
    def test_path_a_less_than_b(self):
        m = ModuloGCD(4, 10, 5)  # GCD = 2
        self.assertEqual(m.cmmdc(), 2 % 5)

    # Path 4: Invalid c (c <= 0)
    def test_path_invalid_c(self):
        with self.assertRaises(ValueError):
            ModuloGCD(10, 5, 0).cmmdc()

    # Path 5: Invalid input type or <= 0 value
    def test_path_invalid_type_or_value(self):
        with self.assertRaises(ValueError):
            ModuloGCD("10", 5, 3).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(10, -5, 3).cmmdc()

    # Path 6: Loop runs too many iterations → RuntimeError
    def test_path_max_iterations_exceeded(self):
        with self.assertRaises(RuntimeError):
            ModuloGCD(999999, 1, 3).cmmdc()
    

if __name__ == "__main__":
    unittest.main()

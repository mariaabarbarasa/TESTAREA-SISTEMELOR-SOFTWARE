import unittest
from ModuloGCD import ModuloGCD

class ModuloGCDTest(unittest.TestCase):
    """1) Partitionare de echivalenta"""
    
    def test_G111_valid_imputs(self):
        result=ModuloGCD(10, 5, 2).cmmdc()
        self.assertEqual(result,1)
        
    def test_G211_invalid_a(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-5,5,2).cmmdc()
       
    def test_G121_invalid_b(self):
        with self.assertRaises(ValueError):
            ModuloGCD(50,"5",4).cmmdc()
    
    def test_G112_invalid_c(self):
        with self.assertRaises(ValueError):
            ModuloGCD(43,5,-2).cmmdc()
            
    def test_G122_invalid_b_c(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-5,5,2).cmmdc()
            
    def test_G212_invalid_a_c(self):
        with self.assertRaises(ValueError):
            ModuloGCD(100.2,31,None).cmmdc()
            
    def test_G221_invalid_a_b(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-5,32.2,6).cmmdc()
            
    def test_G222_invalid_a_b_c(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-5,15.2,"12").cmmdc()
            
    """2) Analiza valorilor de frontiera"""
    
    def test_a_zero(self):
        with self.assertRaises(ValueError):
            ModuloGCD(0, 5, 2).cmmdc()
            
    def test_a_one(self):
        result=ModuloGCD(1, 10, 3).cmmdc()
        self.assertEqual(result,1)
        
    def test_a_two(self):
        result=ModuloGCD(2,5,2).cmmdc()
        self.assertEqual(result,1)
        
    def test_b_zero(self):
        with self.assertRaises(ValueError):
            ModuloGCD(7, 0, 3).cmmdc()
            
    def test_b_one(self):
        result=ModuloGCD(21, 1, 5).cmmdc()
        self.assertEqual(result,1)
        
    def test_b_two(self):
        result=ModuloGCD(14,2,7).cmmdc()
        self.assertEqual(result,2)
        
    def test_c_zero(self):
        with self.assertRaises(ValueError):
            ModuloGCD(7, 21, 0).cmmdc()
            
    def test_c_one(self):
        result=ModuloGCD(33, 11, 1).cmmdc()
        self.assertEqual(result,0)
        
    def test_c_two(self):
        result=ModuloGCD(15,3,2).cmmdc()
        self.assertEqual(result,1)
    
    """3) Acoperire la nivel de instructiune"""

    def test_statement_coverage1(self):
        result=ModuloGCD(43, 17, 2).cmmdc()
        self.assertEqual(result, 1)
        
    def test_statement_convergence2(self):
        result=ModuloGCD(7, 19, 3).cmmdc()
        self.assertEqual(result, 1)
        
    """4) Acoperire la nivel de decizie"""
    
    def test_decision_invalid_input(self):
        with self.assertRaises(ValueError):
            ModuloGCD("10",5,2).cmmdc()
            
    def test_decision_loop_skip(self):
        result=ModuloGCD(10,10,12).cmmdc()
        self.assertEqual(result,10)
        
    def test_decisio_loop_true_branch(self):
        result=ModuloGCD(14,10,5).cmmdc()
        self.assertEqual(result,2)
        
    """5) Acoperire la nivel de conditie"""
    
    def test_condition_isinstance_fail(self):
        with self.assertRaises(ValueError):
            ModuloGCD("9",4,3).cmmdc()
            
    def test_condition_value_fail(self):
        with self.assertRaises(ValueError):
            ModuloGCD(10,-2,3).cmmdc()
            
    def test_condition_true_while(self):
        result=ModuloGCD(4,6,6).cmmdc()
        self.assertEqual(result,2)
        
    def test_condition_false_while(self):
        result=ModuloGCD(3,3,6).cmmdc()
        self.assertEqual(result,3)
        
    def test_condition_true_if(self):
        result=ModuloGCD(4,1,5).cmmdc()
        self.assertEqual(result,1)
        
    def test_condition_false_if(self):
        result=ModuloGCD(1,3,10).cmmdc()
        self.assertEqual(result,1)
        
    """6) Testarea circuitelor independente"""
    
    def test_exit_isinstance(self):
        with self.assertRaises(ValueError):
            ModuloGCD("10",3,6).cmmdc()
            
    def test_exit_value(self):
        with self.assertRaises(ValueError):
            ModuloGCD(10,3.3,6).cmmdc()
            
    def test_exit_both(self):
        with self.assertRaises(ValueError):
            ModuloGCD("10",3.3,6).cmmdc()
            
    def test_exit_a_egal_b(self):
        result=ModuloGCD(10, 10, 12).cmmdc()
        self.assertEqual(result,10)
        
    def test_exit_loop_executed(self):
        result=ModuloGCD(55, 10, 12).cmmdc()
        self.assertEqual(result,5)
        
if __name__ == '__main__':
    unittest.main()
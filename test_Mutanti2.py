import unittest
from ModuloGCD import ModuloGCD

class ModuloGCDTest(unittest.TestCase):
    """Partitionare de echivalenta"""

    def test_valid_inputs(self):
        self.assertEqual(ModuloGCD(10,5,3).cmmdc(),2)
        self.assertEqual(ModuloGCD(15, 10,4).cmmdc(),1)
        self.assertEqual(ModuloGCD(8,12,5).cmmdc(),4)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            ModuloGCD(-5,5,2).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(50,'5',4).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(10,5,0).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(5,-5,-2).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(100.2,31,None).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(-5,32.2,6).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(-5,15.2,'12').cmmdc()

    """Analiza valorilor de frontiera"""

    def test_boundary_values(self):
        with self.assertRaises(ValueError):
            ModuloGCD(0,5,2).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(7,0,3).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(7,21,0).cmmdc()
            
        
        self.assertEqual(ModuloGCD(1,10,3).cmmdc(),1)
        self.assertEqual(ModuloGCD(2,5,2).cmmdc(),1)
        self.assertEqual(ModuloGCD(21,1,5).cmmdc(),1)
        self.assertEqual(ModuloGCD(14,2,7).cmmdc(),2)
        self.assertEqual(ModuloGCD(33,11,1).cmmdc(),0)
        self.assertEqual(ModuloGCD(15,3,2).cmmdc(),1)

    """Acoperire la nivel de instructiune"""

    def test_instruction_coverage(self):
        self.assertEqual(ModuloGCD(43,17,2).cmmdc(),1)
        self.assertEqual(ModuloGCD(7,19,3).cmmdc(),1)
        self.assertEqual(ModuloGCD(14,7,4).cmmdc(),3)

    """Acoperire la nivel de decizie"""

    def test_decision_coverage(self):
        self.assertEqual(ModuloGCD(10,10,12).cmmdc(),10)
        self.assertEqual(ModuloGCD(14,10,5).cmmdc(),2)
        self.assertEqual(ModuloGCD(6,9,7).cmmdc(),3)
        
        with self.assertRaises(ValueError):
            ModuloGCD('10',5,2).cmmdc()

    """Acoperire la nivel de conditie"""

    def test_condition_coverage(self):
        with self.assertRaises(ValueError):
            ModuloGCD('9',4,3).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(10,-2,3).cmmdc()
            
        
        self.assertEqual(ModuloGCD(4,6,6).cmmdc(),2)
        self.assertEqual(ModuloGCD(3,3,6).cmmdc(),3)
        self.assertEqual(ModuloGCD(4,1,5).cmmdc(),1)
        self.assertEqual(ModuloGCD(1,3,10).cmmdc(),1)

    """Testarea circuitelor independente"""

    def test_independent_paths(self):
        with self.assertRaises(ValueError):
            ModuloGCD('10',3,6).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD(10,3.3,6).cmmdc()
        with self.assertRaises(ValueError):
            ModuloGCD('10',3.3,6).cmmdc()
            
        self.assertEqual(ModuloGCD(10,10,12).cmmdc(),10)
        self.assertEqual(ModuloGCD(55,10,12).cmmdc(),5)

if __name__ == '__main__':
    unittest.main()

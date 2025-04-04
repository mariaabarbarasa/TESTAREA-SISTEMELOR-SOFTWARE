import unittest
from multiprocessing import Process
from ModuloGCD2 import ModuloGCD

def run():
    obj=ModuloGCD(10, 10, 5)
    obj.cmmdc_mutant2()
    
class ModuloGCDTestMutant(unittest.TestCase):
    """1) Testare mutant de ordin 1"""
    def test_mutant1(self):
        obj=ModuloGCD(4,4,2)
        correct=obj.cmmdc()
        mutant=obj.cmmdc_mutant1()
        self.assertNotEqual(mutant,correct,"Mutantul 1 trebuie omorat cand a==b")
        
    """2) Testare mutant de ordin 2"""
    def test_mutant2(self):
        proc=Process(target=run)
        proc.start()
        proc.join(timeout=1)
        
        if proc.is_alive():
            proc.terminate()
            proc.join()
            self.fail("Mutantul 2 a intrat in loop infinit")
        
    """3) Testare weak mutation"""
    def test_weak_mutant(self):
        obj=ModuloGCD(10, 6, 4)
        correct=obj.cmmdc()
        result=obj.cmmdc_weak_mutant()        
        self.assertNotEqual(result,correct, "Weak mutation supravietuieste")
        
    """4) Testare strong mutation"""
    def test_strong_mutant(self):
        obj=ModuloGCD(21,6,4)
        correct=obj.cmmdc()
        result=obj.cmmdc_strong_mutant()
        self.assertNotEqual(correct,result,"Strong mutation detected")
        
    """5) Testarea mutant echivalent"""
    def test_equivalent_mutant(self):
        obj=ModuloGCD(32,8,5)
        correct=obj.cmmdc()
        result=obj.cmmdc_mutant_echivalent()
        self.assertNotEqual(correct,result,"Mutantul echivalent ar trebui sa supravietuiasca testarii")
    
    """6) Testarea mutanti neechivalenti"""
    def test_mutant_neechivallent1(self):
        obj=ModuloGCD(12,4,5)
        correct=obj.cmmdc()
        result=obj.cmmdc_mutant_neechivalent1()
        self.assertNotEqual(correct,result,"Mutantul neechivalent 1 trebuie omorat")
            
    def test_mutant_neechivallent2(self):
        obj=ModuloGCD(14,7,4)
        correct=obj.cmmdc()
        result=obj.cmmdc_mutant_neechivalent2()
        self.assertNotEqual(correct,result,"Mutant neechivalent 2 trebuie omorat")
if __name__ == '__main__':
    unittest.main()
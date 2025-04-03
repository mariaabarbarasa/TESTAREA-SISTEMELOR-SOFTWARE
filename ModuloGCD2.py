#Pentru mutanti

class ModuloGCD:
    def __init__ (self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def validate_integer(self,value):
        if not isinstance(value,int) or value<=0:
            raise ValueError("Valorile trebuie sa fie numere naturale pozitive")
            
        return value
    
    #Functia originala
    def cmmdc(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        return a%c
    
    """1) Mutanti de primul ordin"""
    def cmmdc_mutant1(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a>=b: # >= in loc de >
                a=a-b
            else:
                b=b-a
        return a%c
    
    """2) Mutanti de ordinul 2"""
    def cmmdc_mutant2(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a>=b: # >= in loc de !=
            if a<b: # < in loc de >
                a=a-b
            else:
                b=b-a
        return a%c
    
    """3) Weak mutation"""
    def cmmdc_weak_mutant(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a>b:
                a=a-b+0 # am adaugat +0
            else:
                b=b-a
        return a%c
    
    """4) Strong mutation"""
    def cmmdc_strong_mutant(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a>b:
                a=a-b
            else:
                b=b-a
        return a-c # - in loc de %
    
    """5) Mutanti echivalenti"""
    def cmmdc_mutant_echivalent(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a<b: #Am inversat ordinea conditiei
                b=b-a
            else:
                a=a-b 
        return a%c
    
    """6) Testam 2 mutanti neechivalenti"""
    def cmmdc_mutant_neechivalent1(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a>=b:
                a=a-b
            else:
                b=b-a
        return a%b #a%b in loc de a%c
    
    def cmmdc_mutant_neechivalent2(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)
        while a!=b:
            if a>=b: 
                a=a-b
            else:
                b=b-a
        return a&c
    
        
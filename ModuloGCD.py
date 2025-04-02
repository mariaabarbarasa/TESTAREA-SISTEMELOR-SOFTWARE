class ModuloGCD:
    def __init__ (self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def validate_integer(self,value):
        if not isinstance(value,int) or value<=0:
            raise ValueError("Valorile trebuie sa fie numere naturale pozitive")
            
        return value
    

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
    
print(ModuloGCD(15, 5, 12).cmmdc())
class ModuloGCD:
    def __init__(self, a, b, c):
        self.a=a
        self.b=b
        self.c=c

    def validate_integer(self,value):
        if not isinstance(value,int) or value<=0:
            raise ValueError('Valorile trebuie sa fie numere naturale pozitive')
        return value

    def cmmdc(self):
        a=self.validate_integer(self.a)
        b=self.validate_integer(self.b)
        c=self.validate_integer(self.c)

        max_iterations=1000
        iterations=0

        if c<=0:
            raise ValueError('Modulo trebuie sa fie pozitiv')

        if a==b:
            return a%c

        while a!=b:
            if iterations>max_iterations:
                raise RuntimeError('Prea multe iteratii (posibil loop infinit)')
            iterations+=1

            if a>b:
                a=a-b
            else:
                b=b-a

        return a%c
    
13,14,15,17,18,20,23,26,36
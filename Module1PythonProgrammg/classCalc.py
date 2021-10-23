class Calc:
    def sumnum(self, n, m):
        print(n, " + ",m," = ", n + m)

    def multnum(self, n, m):
        print(n, " * ",m," = ",n * m)

    def divnum(self, n, m):
        print(n, " / ",m," = ",n / m)

    def subnum(self, n, m):
        print(n, " - ",m," = ",n - m)

    def allFourBasicCalculations(self, n, m):
        self.sumnum(n,m)
        self.subnum(n, m)
        self.divnum(n, m)
        self.multnum(n, m)

C1=Calc()
C1.allFourBasicCalculations(45 ,34)




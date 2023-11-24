class calc: 
    def __init__(self,a,b):
        self.a = a
        self.b = b
    #    self.c = c 
    def add(self):
        answer = self.a + self.b
        print(answer)
    def sub(self):
        answer = self.a - self.b
        print(answer)
    def mult(self):
        answer = self.a*self.b
        print(answer)
    def div(self):
        answer = self.a / self.b 
        print(answer)
c1 = calc(20,30)
c1.mult()
c1.add()
c1.sub()
c1.div()
c2 = calc(90,50)
c2.mult()
c2.add()
c2.sub()
c2.div()



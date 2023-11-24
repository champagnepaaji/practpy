class calc: 
    def __init__(self,a,b):
        self.a = a
        self.b = b 
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

class mobile:              
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def display_name(self):
        print(self.name)
    def model_name(self):
        print(self.model)

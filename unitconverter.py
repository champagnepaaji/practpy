
class uc: 
    def __init__(self,value):
        self.v = value
    def cm_to_m(self):
        v = self.v/100
        print(self.v,"cm = ",v," m ")
    def m_to_cm(self):
        v = self.v*100
        print(self.v," m =",v,"cm")
    def cm_to_inches(self):
        v = self.v/2.54
        print(self.v,'cm =',v,'inches')
    def inches_to_cm(self):
        v = self.v*2.54
        print(self.v,'inches = ',v,'cm')
            
    
        
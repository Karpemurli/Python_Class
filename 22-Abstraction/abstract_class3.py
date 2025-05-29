from abc import ABC,abstractmethod

class Bank(ABC):
    @abstractmethod
    def get_interest_rate(self):
        pass
    
    @abstractmethod
    def display_info(self):
        pass
    
class SBI(Bank):
    
    def __init__(self,name,int_rate):
        self.name=name
        self.int_rate=int_rate
        
    def get_interest_rate(self):
        return self.int_rate
    
    def display_info(self):
        print("Bank Name= ",self.name)
        print("Interest Rate =",sbi.get_interest_rate())
        
class HDFC(Bank):
    
    def __init__(self,name,int_rate):
        self.name=name
        self.int_rate=int_rate
        
    def get_interest_rate(self):
        return self.int_rate
    
    def display_info(self):
        print("Bank Name= ",self.name)
        print("Interest Rate =",hdfc.get_interest_rate())
        
        
class BOI(Bank):
    
    def __init__(self,name,int_rate):
        self.name=name
        self.int_rate=int_rate
        
    def get_interest_rate(self):
        return self.int_rate
    
    def display_info(self):
        print("Bank Name= ",self.name)
        print("Interest Rate =",boi.get_interest_rate())
        
        
# create the object each class     
sbi=SBI("SBI Bank", 8.5)
hdfc=HDFC("HDFC Bank", 9.0)
boi=BOI("BOI Bank", 8.6)


sbi.display_info()
hdfc.display_info()
boi.display_info()


        
        
        
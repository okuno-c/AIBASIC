from .database import Database
class Information:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        self.__csvfile = 'infoemation.csv'
    def information(self,wtype):
        print("Name: {} \n Age: {} \ Address: {} \n".format(self.name,self.age,self.address))
    def saveinformation(self,wtype):
        student = [self.name,self.age,self.address,wtype]
        Database([student],self.__csvfile).savedata()
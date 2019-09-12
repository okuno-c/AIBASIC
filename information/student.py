from information import Information

class Student(Information):
    def __init__(self,name,age,address,yearlvl):
        super().__init__(name,age,address)
        self.yearlvl = yearlvl
    def studentinfo(self):
        print(" Name:{}\n Age:{}\n Address:{}\n Yearlvl:{}".format(self.name,self.age,self.address,self.yearlvl))
    def addstudent(self):
        super().saveinformation('student')
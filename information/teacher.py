from information import Information

class Teacher(Information):
    def __init__(self,name,age,address):
        super().__init__(name,age,address)
    def teacherinfo(self):
        print(" Name:{}\n Age:{}\n Address:{}\n Yearlvl:{}".format(self.name,self.age,self.address))
    def addteacher(self):
        super().saveinformation('teacher')
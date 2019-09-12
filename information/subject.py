from .database import Database

class Subject:
    def __init__(self,subject_name,subject_code):
        self.subject_name = subject_name
        self.subject_code = subject_code
        self.__csvfile = 'data/subject.csv'
        
    def subjectinfo(self):
        print("Name:{}\n Code:{}".format(self.subject_name,self.subject_code))

    def addsubject(self):
        last_id = Database([],self.__csvfile).id_ai()
        subject = [last_id+1,self.subject_name,self.subject_code]
        Database([subject],self.__csvfile).savedata()

    def allsubject(self):
        print(Database().readdata())
        
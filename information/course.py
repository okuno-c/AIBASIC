from .database import Database

class Course:
    def __init__(self,course_name,course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.__csvfile = 'data/course.csv'
        
    def courseinfo(self):
        print("Name:{}\n Code:{}".format(self.course_name,self.course_code))

    def addcourse(self):
        last_id = Database([],self.__csvfile).id_ai()
        course = [last_id+1,self.course_name,self.course_code]
        Database([course],self.__csvfile).savedata()

    def allcourse(self):
        print(Database().readdata())
        
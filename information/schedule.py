from .database import Database

class Schedule:
    def __init__(self,schedule_name,schedule_code):
        self.schedule_name = schedule_name
        self.schedule_code = schedule_code
        self.__csvfile = 'data/schedule.csv'
        
    def scheduleinfo(self):
        print("Name:{}\n Code:{}".format(self.schedule_name,self.schedule_code))

    def addschedule(self):
        last_id = Database([],self.__csvfile).id_ai()
        course = [last_id+1,self.schedule_name,self.schedule_code]
        Database([schedule],self.__csvfile).savedata()

    def allschedule(self):
        print(Database().readdata())
        
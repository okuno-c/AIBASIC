import csv
class Database:
    def __init__(self,data=[],filename=''):
        self.data = data
        self.header = []
        self.filename = filename
        self.last_id = 0

    def savedata(self):
        self.readdata()
        with open(self.filename,'w',newline='') as wf:
            writer = csv.writer(wf)
            writer.writerow(self.header)
            writer.writerows(self.data)

    def readdata(self):
        with open(self.filename,'r') as rf:
            reader = csv.reader(rf)
            self.header = next(reader)
            for row in reader:
                self.data.append(row)
        return self.data

    def id_ai(self):
        with open(self.filename,'r') as rf:
            reader = csv.reader(rf)
            self.header = next(reader)
            if reader:
                self.last_id = len(list(reader))
        return self.last_id
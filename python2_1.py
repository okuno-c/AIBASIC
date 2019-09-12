# encapsulation
# class Car:
#     def __init__(self):
#         self.__secretkey = '123xxx22'

#     def getter(self):
#         return self.__secretkey
#     def setter(self,seckey):
#         self.__secretkey = seckey

# Car().setter('asdasadsa')
# car1 = Car()
# car1.setter('12344xxxxx')
# print(car1.getter())

# inheritance
# import subprocess as sp

# info_list = []
# class Person:
#     def __init__(self,name,age,address):
#         self.name = name
#         self.age = age
#         self.address = address
#     def (self):
#         print(" Name:{}\n Age:{}\n Address:{}\n".format(self.name,self.age,self.address))
#     def saveinformation(self,wtype):
#         information_dict = {"name":self.name,"age":self.age,"address":self.address,"type":wtype}
#         info_list.append(information_dict)
#     def getinformation(self):
#         return self.info_list

# #Personクラスから継承する
# class Student(Person):
#     def __init__(self,name,age,address,yearlvl):
#         super().__init__(name,age,address)
#         self.yearlvl = yearlvl
#     def studentinfo(self):
#         print(" Name:{}\n Age:{}\n Address:{}\n Yearlvl:{}".format(self.name,self.age,self.address,self.yearlvl))
#     def addstudent(self):
#         super().saveinformation('student')

# class Teacher(Person):
#     def __init__(self,name,age,address):
#         super().__init__(name,age,address)
#     def teacherinfo(self):
#         print(" Name:{}\n Age:{}\n Address:{}\n Yearlvl:{}".format(self.name,self.age,self.address))
#     def addteacher(self):
#         super().saveinformation('teacher')

# class View:
#     @staticmethod
#     def showinfo():
#         print("Name | Age | Address | Type")
#         for info in info_list:
#             print("{} | {} | {} | {} \n".format(info["name"],info["age"],info["address"],info["type"]))

# # student1 = Student("Chika",32,"Tokyo",3)
# # student1.addstudent()
# # teatcher1 = Teacher("Jan",32,"Cebu")
# # teatcher1.addteacher()
# # print(View().showinfo())
# # sp.call('clear',shell =True)

# print("Welcome to Enrollment System!")

# while True:
#     print(" [1] Student")
#     print(" [2] Teacher")
#     print(" [3] ShowInformations")
#     print(" [4] Exit")

#     choice = int(input("Your Choice : "))

#     if choice == 1:
#         sp.call('clear',shell =True)
#         name = input("Input name. : ")
#         age = int(input("Input age. : "))
#         address = input("Input address. : ")
#         yearlvl = int(input("Input yearlvl. : "))
#         student = Student(name,age,address,yearlvl)
#         student.addstudent()
#         sp.call('clear',shell =True)

#     if choice == 2:
#         sp.call('clear',shell =True)
#         name = input("Input name. : ")
#         age = int(input("Input age. : "))
#         address = input("Input address. : ")
#         teacher = Teacher(name,age,address)
#         teacher.addteacher()
#         sp.call('clear',shell =True)

#     if choice == 3:
#         sp.call('clear',shell =True)
#         print(View().showinfo())

#     if choice == 4:
#         break
    
import subprocess as sp

author_list = []
book_list = []

class Author:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def author_list(self):
        return self.author_list
    def author_save(self):
        author_dict = {"name":self.name,"age":self.age,"address":self.address}
        author_list.append(author_dict)

class Book:
    def __init__(self,title,genre,author):
        self.title = title
        self.genre = genre
        self.author = author
    def book_list(self):
        return self.book_list
    def book_save(self):
        book_dict = {"title":self.title,"genre":self.genre,"author":self.author}
        book_list.append(book_dict)

class View:
    @staticmethod
    def showauthor():
        print("Name | Age | Address")
        for info in author_list:
            print("{} | {} | {}".format(info["name"],info["age"],info["address"]))
 
    @staticmethod
    def showbook():
        print("Title | Genre | Author")
        for info in book_list:
            print("{} | {} | {}".format(info["title"],info["genre"],info["author"]))

print("Welcome to Enrollment System!")

while True:
    print(" [1] Input Author")
    print(" [2] Input Book")
    print(" [3] Show Author Informations")
    print(" [4] Show Book Informations")
    print(" [5] Exit")

    choice = int(input("Your Choice : "))

    if choice == 1:
        sp.call('clear',shell =True)
        name = input("  Input name. : ")
        age = int(input("  Input age. : "))
        address = input("  Input address. : ")
        author = Author(name,age,address)
        author.author_save()
        sp.call('clear',shell =True)

    elif choice == 2:
        sp.call('clear',shell =True)

        if len(author_list) == 0:
            continue
        else:
            title = input("Input title. : ")
            genre = input("Input genre. : ")
            for i in range(len(author_list)):
                print("[",i,"]"+" "+author_list[i]["name"])
            author_choice = int(input("Choose Author's No. : "))
            author = author_list[author_choice]["name"]
            book = Book(title,genre,author)
            book.book_save()
            sp.call('clear',shell =True)

    elif choice == 3:
        sp.call('clear',shell =True)
        print(View().showauthor())

    elif choice == 4:
        sp.call('clear',shell =True)
        print(View().showbook())

    elif choice == 5:
        break

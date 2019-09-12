# import math
# import statistics

# print(math.pow(2,3))

# my_list = [2,45,67,23,45]

# mean = statistics.mean(my_list)
# medium = statistics.median(my_list)
# mode = statistics.mode(my_list)
# print(mean)
# print(medium)

# print(dir(statistics))

#1つ目のinformationはフォルダ名
from information.information import Information
from information.student import Student
from information.teacher import Teacher
from information.database import Database
from information.subject import Subject
from information.course import Course
from information.schedule import Schedule
import subprocess as sp

# class View:
#     @staticmethod
#     def showinfo():
#         print("Name | Age | Address | Type")
#         for info in info_list:
#             print("{} | {} | {} | {} \n".format(info["name"],info["age"],info["address"],info["type"]))

# print("Welcome to Enrollment System!")

while True:
    print(" [1] Student")
    print(" [2] Teacher")
    print(" [3] Course")
    print(" [4] Subject")
    print(" [5] Schedule")
    print(" [6] ShowInformations")
    print(" [0] Exit")

    choice = int(input("Your Choice : "))

    if choice == 1:
        sp.call('clear',shell =True)
        name = input("Input name. : ")
        age = int(input("Input age. : "))
        address = input("Input address. : ")
        yearlvl = int(input("Input yearlvl. : "))
        student = Student(name,age,address,yearlvl)
        student.addstudent()
        sp.call('clear',shell =True)

    if choice == 2:
        sp.call('clear',shell =True)
        name = input("Input name. : ")
        age = int(input("Input age. : "))
        address = input("Input address. : ")
        teacher = Teacher(name,age,address)
        teacher.addteacher()
        sp.call('clear',shell =True)

    if choice == 3:
        sp.call('clear',shell =True)
        course_name = input("Input course name. : ")
        course_code = input("Input course code. : ")
        course = Course(course_name,course_code)
        course.addcourse()
        sp.call('clear',shell =True)

    if choice == 4:
        sp.call('clear',shell =True)
        subject_name = input("Input subject name. : ")
        subject_code = input("Input subject code. : ")
        subject = Subject(subject_name,subject_code)
        subject.addsubject()
        sp.call('clear',shell =True)

    if choice == 5:
        sp.call('clear',shell =True)
        schedule_name = input("Input schedule name. : ")
        schedule_code = input("Input schedule code. : ")
        schedule = Schedule(schedule_name,schedule_code)
        schedule.addschedule()
        sp.call('clear',shell =True)

    if choice == 6:
        print(Database().readdata())

    if choice == 0:
        break

# from information.database import Database
# import csv

# while True:
#     name = input("enter your name : ")
#     age = input("enter your age : ")
#     address = input("enter your address : ")
#     types = input("enter your types : ")
#     choice = input("You want to add more? y/n : ")
#     Database([[name,age,address,types]]).savedata(['name','age','address','types'])

#     if choice == "y":
#         continue
#     else:
#         break




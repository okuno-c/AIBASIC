
# class Robot:
#     def __init__(self,name="Lorem"):
#         self.name = name
#         self.color = "Red"
#         self.energy = 100

#     def introduce_yourself(self):
#         print("My name is "+self.name)
    
#     def jump(self):
#         if self.energy > 50:
#             print("I can fly!")
#             self.energy -= 10
#         if self.energy <= 50 and self.energy >= 10:
#             print("Low energy")
#             self.energy -= 10
#         elif self.energy == 0:
#             print("Empty energy")
#         return self.energy

#     def ener(self):
#         print(self.name+"'s energy left are ",self.energy)
    
#     @staticmethod
#     def newfunc():
#         return True

# robot1 = Robot("Tom")
# robot1.introduce_yourself()
# robot1.ener()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# robot1.jump()
# robot1.ener()

# class Car:
#     def __init__(self,brand,color,unitcode):
#         self.brand = brand
#         self.color = color
#         self.unitcode = unitcode
#         self.speed = 0
#         self.speedlimit = 160
#         self.fuel = 0
#         self.fuellimit = 40
    
#     def info(self):
#         print("Brand: "+self.brand+", Color: "+self.color+", Unitcode:",self.unitcode,".")

#     def speedup(self):
#         if self.fuel >= 2:
#             self.fuel -= 2
#             if self.speed < self.speedlimit:
#                 self.speed += 10
#                 print("Your speed is",self.speed,".")
#             else:
#                 print("You are in Speedlimit!")
#         else:
#             print("Empty gas.")

#     def speeddown(self):
#         if self.speed >= 10:
#             self.speed -= 10
#             print("Your speed is",self.speed,".")
#         else:
#             print("Stopped.")

#     def gasup(self):
#         if self.fuel < self.fuellimit:
#             self.fuel += 5
#             print("Your fuel is",self.fuel,".")
#         else:
#             print("You are in Fuellimit!")

#     def gasdown(self):
#         if self.fuel > 0:
#             self.fuel -= 5
#             print("Your fuel is",self.fuel,".")
#         else:
#             print("Empty gas.")

# print("Create Your Car now !!")
# brand = input("Input brand : ")
# color = input("Input color : ")
# unitcode = input("Input unitcode : ")

# Toyota = Car(brand,color,unitcode)

# while True:
#     print("[1]info()")
#     print("[2]speedup()")
#     print("[3]speeddown()")
#     print("[4]gasup()")
#     print("[5]gasdown()")

#     choice = int(input("Choose an operator to perform : "))

#     if choice == 1:
#         Toyota.info()
#     elif choice == 2:
#         Toyota.speedup()
#     elif choice == 3:
#         Toyota.speeddown()
#     elif choice == 4:
#         Toyota.gasup()
#     elif choice == 5:
#         Toyota.gasdown()
#     else:
#         print("Your car has stopped.")
#         break

#追加課題
class Car:
    def __init__(self,brand,color,unitcode):
        self.brand = brand
        self.color = color
        self.unitcode = unitcode
        self.speed = 0
        self.speedlimit = 160
        self.fuel = 0
        self.fuellimit = 40

    def info(self):
        print("Brand: "+self.brand+", Color: "+self.color+", Unitcode:",self.unitcode,".")

    def speedup(self):
        if self.fuel >= 2:
            self.fuel -= 2
            if self.speed < self.speedlimit:
                self.speed += 10
                print("Your speed is",self.speed,".")
            else:
                print("You are in Speedlimit!")
        else:
            print("Empty gas.")

    def speeddown(self):
        if self.speed >= 10:
            self.speed -= 10
            print("Your speed is",self.speed,".")
        else:
            print("Stopped.")

    def gasup(self):
        if self.fuel < self.fuellimit:
            self.fuel += 5
            print("Your fuel is",self.fuel,".")
        else:
            print("You are in Fuellimit!")

    def gasdown(self):
        if self.fuel > 0:
            self.fuel -= 5
            print("Your fuel is",self.fuel,".")
        else:
            print("Empty gas.")

car_list = []

count = int(input("How many cars do you create? : "))

for i in range(count):
    car_dict = {}
    print("Create Your Car now !!")
    car_dict["brand"] = input("  Input brand : ")
    car_dict["color"] = input("  Input color : ")
    car_dict["unitcode"] = input("  Input unitcode : ")
    car_dict["self"] = Car(car_dict["brand"],car_dict["color"],car_dict["unitcode"])

    car_list.append(car_dict)

for i in range(0,count):
    print("[",i+1,"] "+car_list[i]["unitcode"]+" "+car_list[i]["brand"])

choice_c = int(input("Which car do you operate? : "))
print("Your choice is [",choice_c,"] "+car_list[choice_c-1]["unitcode"]+" "+car_list[choice_c-1]["brand"])

while True:
    print("  [1]info()")
    print("  [2]speedup()")
    print("  [3]speeddown()")
    print("  [4]gasup()")
    print("  [5]gasdown()")

    choice_o = int(input("Choose an operator to perform : "))

    if choice_o == 1:
        car_list[choice_c-1]["self"].info()
    elif choice_o == 2:
        car_list[choice_c-1]["self"].speedup()
    elif choice_o == 3:
        car_list[choice_c-1]["self"].speeddown()
    elif choice_o == 4:
        car_list[choice_c-1]["self"].gasup()
    elif choice_o == 5:
        car_list[choice_c-1]["self"].gasdown()
    else:
        print("Your car has stopped.")
        break



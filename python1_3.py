
# y = 1**2+3*1+2

# def f(x):
#     y = x**2+3*x+2
#     print(y)

# f(10)

# def add(x,y):
#     total = x + y
#     return total

# add(2,4)
# print(add(2,4)*add(3,5))

# def even_odd():
#     n = int(input("Enter a number : "))
#     if n%2 ==0:
#         print(n,"is even number.")
#     else:
#         print(n,"is an odd number.")

# even_odd()

# #1
# def multiply(x,y):
#     answer = x*y
#     return answer

# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))

# num3 = multiply(num1,num2)

# print("Answer is",num3)

# #2
# def hello(x):
#     for i in range(0,x):
#         print("Hello world!")

# num = int(input("Enter a number : "))
# hello(num)

# number = [1,2,3,4,5,6,7]
# print(max(number))

# #4
# def shopping(time,val,num):
#     sum = val * num
#     if num >= 5:
#         sum = sum*0.9
#     if time > 15 and 24 > time:
#         sum = sum*0.9
#     return sum

# name = input("What is your name? : ")
# time = int(input("What time is it now?(0-24) : "))
# val = int(input("How much is the item? : "))
# num = int(input("How many? : "))

# print("Total amount of "+name+" is",shopping(time,val,num),".")

#5
# def f_add(x,y):
#     print("You choose addition.")
#     print("Answer is",x+y)
# def f_sub(x,y):
#     print("You choose substraction.")
#     print("Answer is",x-y)
# def f_mul(x,y):
#     print("You choose multiplication.")
#     print("Answer is",x*y)
# def f_div(x,y):
#     print("You choose division.")
#     print("Answer is",x/y)

# while True:
#     print("[1] addition")
#     print("[2] subtraction")
#     print("[3] multiplication")
#     print("[4] divition")

#     num1 = int(input("Enter a nubmer1 : "))
#     num2 = int(input("Enter a nubmer2 : "))
#     choice = int(input("Choose an operator to perform : "))

#     if choice == 1:
#         f_add(num1,num2)
#     elif choice == 2:
#         f_sub(num1,num2)
#     elif choice == 3:
#         f_mul(num1,num2)
#     elif choice == 4:
#         f_div(num1,num2)

#     cont = input("Do you want to continue?(y/n) : ")
#     if cont == "n":
#         break

class MyCar:
    def __init__(self,brand,color,code):
        self.brand = brand
        self.color = color
        self.code = code
        self.speed = 0

        print("Car brand {},color {},code{}".format(self.brand,self.color,self.code))

    def speedup(self):
        self.speed += 10
        return self.speed

Toyota = MyCar('Toyota','Red','x009')
Isuzu = MyCar('Isuzu','Black','x010')

while True:
    speed = input("enter st/si to speedup : ")
    if speed == "st":
        print("Your car",Toyota.brand," speed is ",Toyota.speedup())
        continue
    if speed == "si":
        print("Your car",Isuzu.brand," speed is ",Isuzu.speedup())
        continue
    else:
        break



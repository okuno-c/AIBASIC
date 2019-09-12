
# x = 10//2
# print(x)

# x = not 9>8 or 8<10
# print(x)

# name = "chika"
# age = 32
# print("my name is {} and i am {} years old".format(name,age))

# """
# x = 10
# print(x)
# """

# name = "My name is Chika."
# print(name[0])
# #この方法で内容を書き換えることはできない
# print(name.split(" "))

# splitedname = name.split(" ")
# print('@'.join(splitedname))

# name = "          chika     "
# print(name)
# print(name.strip())

# age = int(input("How young are you? :"))
# if age >= 20 and age < 60:
#     print("You are in legal age.")
# elif age >= 60 and age < 120:
#     print("You are already sinior.")
# else:
#     print("You are under age.")

# students = [{"name":"hiro"},{"name":"chika"},{"name":"asuka"}]

# for student in students:
#     print(student["name"])

# x = 0
# while True:
#     question = input("Do you want to quit? Y/N : ")
#     if question == "Y":
#         break
#     else:
#         continue

#1
# while True:
#     num = int(input("Enter a number : "))
#     if num == 100:
#         break
#     else:
#         continue

#2
# num = int(input("Enter a number : "))
# for i in range(1,num):
#     if i%2==0:
#         print(i)

#1
# num = int(input("Enter a number : "))
# roman = ""

# while num >= 1000:
#     roman = roman + "M"
#     num = num - 1000

# while num >= 500:
#     roman = roman + "D"
#     num = num - 500

# while num >= 100:
#     roman = roman + "C"
#     num = num - 100

# while num >= 50:
#     roman = roman + "L"
#     num = num - 50

# while num >= 10:
#     roman = roman + "X"
#     num = num - 10

# while num >= 9:
#     roman = roman + "IX"
#     num = num - 9

# while num >= 5:
#     roman = roman + "V"
#     num = num - 5

# while num >= 4:
#     roman = roman + "IV"
#     num = num - 4

# while num >= 1:
#     roman = roman + "I"
#     num = num - 1

# print(roman)

#2
roman_dic = {"M":1000,"D":500,"C":100,"L":50,"X":10,"IX":9,"V":5,"IV":4,"I":1}
roman = input("Enter a roman numeral : ")

roman_list = list(roman)
print(roman_list)

num = 0
mem = ""
flag = 0

for roman in roman_list:

    if roman == "I" and flag == 0:
        flag = 1
        mem += roman
        continue

    if flag == 1:
        mem += roman
        flag = 0
        if mem == "IX":
            num += 9
            mem = ""
            continue
        elif mem == "IV":
            num += 4
            mem = ""
            continue
        else:
            num += 1
            mem = ""

    num += roman_dic[roman]

if mem == "I":
    num += roman_dic[mem]

print(num)



















# ■■■■■■■■■■■■参考■■■■■■■■■■■■
# #ローマ数字を値変換したい。ただし、IVとIXは２文字１セットで判断したい。
# for roman in roman_list:
#     #ローマ数字がIの場合は次の文字もセットで判断するためmemに格納する。
#     #memに複数回Iが入ることはない。
#     if roman == "I" and mem == "":
#         mem += roman
#         continue
#     #前回の値がIの場合、今回の値がV、Xだったら２文字１セットで判定する。
#     elif mem != "" and (roman == "V" or roman == "X"):
#         num += roman_dic[mem + roman]
#         mem = ""
#     #上記以外の場合は今回の値のみで判定する。
#     else:
#         num += roman_dic[roman]

# #memに値が残っている場合はその値を判定する。
# if mem != "":
#     num += roman_dic[mem]

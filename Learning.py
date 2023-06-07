###Learn python it is really simple
from ast import If
from gettext import translation
from math import *
import string
from unittest import result
#
# ---------------------Custom Print statement--------------------------------
#
def log (value):
    print(value)
#
#
snake_case = "Hello python where you at?"
# print(snake_case.lower().isupper()) #len() .index()
# print(snake_case.replace("python","JavaScript"))
#
###-------------------Playing around with inbuilt math functions.---------------------
#
abstract = abs(-4) #gives abstract
powered = pow(4, 2)
maximum = max(4, 7) #checks for the maximum
minimum = min(4, 7)
rounded = round(4.3)
ceilled = ceil(4.3)
floored = floor(5.7)
rooted = sqrt(16)
#
###----------------Working with strings----------------------------
#
#name=input("Please enter your name : ")
#print(f"Hello {name} looking great with the progress.")
num1: int = 23   #with the old syntax you have to use int(num1)
num2: int = 12
#print(num1+num2)
#
# ##----------------Working with arrays--------------------------
#
my_array = ["Hello", 34, "Jaymo", 56, "maeto"]
my_array2 = [23, 45, 3, 7, 96, 8]
my_array2.extend(my_array)
#.append(what_to_append) .insert(index_to_insert,what_to_insert)
# .remove(what_to_remove) .pop()=>removes last element .count(what_to_check)=> checks how many times a item is repeated
# .sort()  .reverse()
new_array = my_array.copy()  #coppies an array
# print(new_array)
# print(my_array[1:-2])
#
# FUNCTIONS----------------------functions are defined using def key word--------------------------
#
#
# def hello_user(name):
#     print(f"Hello {name} yes you")
# hello_user("Jaython")
#
# -------------------If else statememts-----------------------
#
# if 12<13 and 3<1:
#     log("gribang")
# elif 12>3:
#     log("brubang")
# else:
#     log("pundeco")
#
# ------------------------Calculator------------------
#
# log("Hello, welcome to my simple calculator!!!!")
# num1:int=input("Please input the first number : ")
# operator=input("Please add your operator : ")
# num2:int=input("Please input the second number : ")

# if operator== '+':
#     log(f"The answer is : {int(num1)+int(num2)}")
# elif operator=='-':
#     log(f"The answer is : {int(num1)-int(num2)}")
# elif operator=='/':
#     log(f"The answer is : {int(num1)/int(num2)}")
# elif operat
#r=='*':
#     log(f"The answer is : {int(num1)*int(num2)}")
# elif num1==string or num2==string:
#     log("Numbers cannot be words!!!!!")
# else:
#     log("Invalid Operator!!!!!!")
#
# --------------------------Dictionaries--------------------
#
# myDictionary={
#     "name":"Mirnova",
#     "age":23,
#     "location":"barth"
# }
# log(myDictionary.get("age","Not a valid key!!!!!"))
# log(myDictionary["name"])
#
# ------------------------------WHILE LOOPS-------------------------
#
# i=0
# while i<=10:
#      log(i)
#      i+=1
#
# -------------------FOR LOOPS--------is more like forEach() in JS-------------------
#
# for curr in my_array:
#     log(curr)
#
# for curr in range(10):
#     log(curr)
# \# for curr in range(3,10):
#     log(curr)
#
# for curr in range(len(my_array)):
#     log(my_array[curr])
#
# --------------------Exponents 3**2-------------------
#
# def raise_to_power(base,raiser):
#     result=1
#     for curr in range(raiser):
#         result=result*base
#     return result
# log(raise_to_power(2,3))
#
# -------------------------------2D arrays------------------------------
# dimArray=[
#     ["Hello",3,"follow"],
#     ["Mello",4,"Bellow"],
#     ["Yellow",5,"Denno"],
#     ["last last"]
# ]
# for currTop in dimArray:
#     for curr in currTop:
#         log(curr)
#
# -----------------------------------Transilator------------------
# def translator(phrase):
#     phrase.lower()
#     translation=''
#     for curr in phrase:
#         if curr in "aeiou":
#             translation+='g'
#         else:
#             translation+=curr
#     return translation
# log(translator(phrase=input("Please add a phrase : ")))
# #
#
# -------------------------------------ERROR Handling-------------------------------
#
# try:
#     num4=int(input("Please add a random number : "))
#     answer=num4/0
# except ValueError as err:
#     log(err)
#     log("Invalid num")
# except ZeroDivisionError:
#     log("Invalid divisor")
#
# -------------------------Opening files---------------------------------
#
myFile = open("./list.txt", "a")  # r r+ w a
mysecondfile = open("./list.txt", "a")
# for curr in mysecondfile.readlines():
#     log(curr)
# log(myFile.readable())
# log(myFile.readline())
# log(myFile.readlines())
# log(myFile.read())
# myFile.close()
# mysecondfile.close()
#
# ------------------------------Writing to files-------------------------
#
# myFile.write("\nHello this is an appending statement.")
#
# ---------------------------------MODULES and PIP-------------------------
#
#
# #---------------------------CLASSES_--------------------------
# class Student :
#     def __init__(self,name,age,location,occupation,education):
#      self.name=name,
#      self.age=age,
#      self.location=location,
#      self.occupation=occupation,
#      self.education=occupation
#
# ------------------------------------Truples-------------------y
# even if  A truple has one item  have to add a coma after
mytruple = ("apple", "banana", "cherry")
if "appl" in mytruple:
    log("hello world")
else:
    log("not")

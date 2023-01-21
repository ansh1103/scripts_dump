import re

# string = "Guru99, learning in awesome 2  and ansh11 is learning"
# res = re.findall(r'^\w+', string)
# print(res)
#
# """Splitting words with split()"""
# res1 = re.split(r's', string)
# print(res1)

#################################################
# class Parent(object):
#     x = 1
#
#
# class Child1(Parent):
#     pass
#
#
# class Child2(Parent):
#     pass
#
#
# print(Parent.x, Child1.x, Child2.x)
#
# Child1.x = 2
# print(Parent.x, Child1.x, Child2.x)
#
# Parent.x = 3
# print(Parent.x, Child1.x, Child2.x)
# ########################################################3
#
# list1 = [[]] * 5
# print(list1)
#
# list1[0].append(10)
# print(list1)
#
# list1[1].append(20)
# print(list1)
#
# list1.append(30)
# print(list1)
#
# #######################################################
# class Car:
#     __maxspeed = 0
#
#     def __init__(self):
#         self.__maxspeed = 200
#
#     def drive(self):
#         print('driving. maxspeed ' + str(self.__maxspeed))
#
#
# redcar = Car()
# redcar.drive()
# redcar.__maxspeed = 300
# redcar.drive()
#
# #############################################
# class Test:
#     def __init__(self):
#         self.x = 0
#
#
# class Derived_Test(Test):
#     def __init__(self):
#         Test.__init__(self)
#         self.y = 1
#
#
# if __name__ == '__main__':
#     b = Derived_Test()
#     print(b.x, b.y)
#
# ###################################################
# a=[10,5]
# a.append(6)
# print(a)
# a.extend([7])
# print(a)
# print(a[:-1])
# print(a[-1:])
# print(a)
#
# #####################
# def star(func):
#     def inner(*args, **kwargs):
#         print("*" * 30)
#         func(*args, **kwargs)
#         print("*" * 30)
#
#     return inner
#
#
# def percent(func):
#     def inner(*args, **kwargs):
#         print("%" * 30)
#         func(*args, **kwargs)
#         print("%" * 30)
#
#     return inner
#
#
# @star
# @percent
# def printer(msg):
#     print(msg)
#
#
# printer("Hello")
###########################################################
"""
# Find the number of repeated words in a file/string
# Print words that are repeated odd number of times and have even number of characters
# input = "Hello my name is Praveen\nAre you done\nMy work is not done\nWhen I am done I will let you know\nIs that so\n"
# is = 3
# done = 3
"""
import re


def func(input_s):
    word_dict = {}
    res = []

    word_list = re.split(' |\n', input_s.lower())
    # word_list = input_s.split(' |\n')

    print(word_list)
    for i in range(len(word_list)):
        if word_list[i] in word_dict.keys():
            word_dict[word_list[i]] += 1
        else:
            word_dict[word_list[i]] = 1
    print(word_dict)

    for key, value in word_dict.items():
        if value > 1 and value % 2 != 0 and len(key) % 2 == 0:
            res.append(key)

    return res

print(func("Hello my name is Praveen\nAre you done\nMy work is not done\nWhen I am done I will let you know\nIs that so\n"))

###############################################################
# Find if a given number is odd or even without using % operator
def func(n):
    if int(n/2) * 2 == n:
        print('even')
    else:
        print('odd')

func(273)

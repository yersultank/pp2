import math
import time
#1 task
# size=int(input("size of list:"))
# list=[]
# for i in range(1,size+1):
#     element=int(input("enter number:"))
#     list.append(element)
# prod=eval('*'.join(map(str,list)))
# print(prod)

#2 task
# s=input("type a string:")
# cnt_upper=sum(1 for i in s if i.isupper())
# cnt_lower=sum(1 for i in s if i.islower())
# print(f"There are {cnt_upper} uppercase letters and {cnt_lower} lowercase letters")

#3 task
# def is_palinfrome(s):
#     return s==s[::-1]
# word=input("type a word:")
# print(is_palinfrome(word))
        
#4 task
# num=int(input("write a number:"))
# mlsec=int(input("choose milliseconds:"))
# num=math.sqrt(num)
# time.sleep(mlsec/1000)
# print(num)

#5 task
# size=int(input("size of tuple:"))
# list=[]
# for i in range(1,size+1):
#     element=input("enter element:")
#     if element==0 or element==False:
#         list.append(0)
#     elif element=="False":
#         list.append(False)
#     elif element=="True":
#         list.append(True)
#     elif element=="1":
#         list.append(1)
#     else:
#         list.append(element)
# tuple=tuple(list)
# x=all(tuple)
# print(x)

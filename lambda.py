
# WAP to define a function for sum, difference, multiplication and division
# a= lambda x,y:x+y
# print(a(10,20))
# b= lambda x,y:x-y
# print(b(100,1))
# c=lambda x,y:x*y
# print(c(33,887))
# d=lambda x,y:x/y
# print(d(100,2))
# # WAP to print the even number from a range by defining functions
# def evenNum(n):
#     even=[]
#     for i in range(1,n+1):
#         if i%2==0:
#             even.append(i)
#     print(even)
# evenNum(10)
#WAP to print square of given numbers
# numbers=[1,2,3,4]
# squared=list(map(lambda x: x**2,numbers))
# print(squared)
# numbers=[1,2,3,4,5]
# even_numbers=list(filter(lambda x:x%2==0,numbers))
# print(even_numbers)
from functools import reduce
numbers=[1,2,3,4]
product=reduce(lambda x,y:x*y,numbers)
print(product)



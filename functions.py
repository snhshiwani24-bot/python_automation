def greet(name):
    return "Hello, " + name

print(greet("Alice"))

def square(x):
    return x*x
print(square(4))

def m(a,b):
    print("be10x")
    print(a+b)

m(22,33)

# WAP to define a function for sum, difference, multiplication and division
x=int(input("enter the num 1 "))
y=int(input("enter the num 2 "))
def sum(x,y):
    print("sum:"+ str(x+y))
sum(x,y)

def sub(x,y):
    print("substraction:"+ str(x-y))
sub(x,y)

def mul(x,y):
    print("multiplication:"+ str(x*y))
mul(x,y)

def div(x,y):
    print("division:"+ str(x/y))
div(x,y)

# WAP to print the even number from a range by defining functions

def evenNum():
    for i in range(50,100):
        if i%2==0:
            print("even number "+str(i))
evenNum()
                    
# 1. Write a Python function to find the maximum of three numbers.
b=[199,111,97]
def maxNum(num):
        if b[0]>=b[1]:
            if b[0]>=b[2]:
                print("largest number is: "+ str(b[0]))
            else:
                print("largest number is: "+ str(b[2]))
        else:
            if b[1]>=b[2]:
                print("largest number is: "+ str(b[1]))
maxNum(b)

# 2. Write a Python function to sum all the numbers in a list.
c=[2,3,4,5,6]
def sumNum(numbr):
    sum=0
    for i in range(0,len(c)):
        sum=sum+c[i]
    print(sum)

sumNum(c)
    
# 3. Write a Python function to multiply all the numbers in a list.

def mulNm(numbr):
    m=1
    for i in range(0,len(c)):
        m=m*c[i]
    print(m)

mulNm(c)

# 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

n=15
def factorial(nm):
    fact=1 
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
factorial(n)

#5. Write a Python program to print the even numbers from a given list.
a=[28,37,28,12,9,873,73,6]
def evenNum(num):
    for i in range(0,len(a)):
        if a[i]%2==0:
            print("print even number "+str(a[i]))
evenNum(a)

#calculate factorial of a number
x=input("given number")
def factorial(n):
    return 1 if (n==0 or n==1) else n*factorial(n-1)
print(factorial(int(x)))


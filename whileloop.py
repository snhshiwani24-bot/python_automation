# Exercise 1: Print first 10 natural numbers using while loop
count=1
while count<=10:
    print(count)
    count+=1

# Exercise 2: Calculate sum of all numbers from 1 to a given number
sum=0
i=1
number=int(input("given number"))
while i<=number:
    sum=sum+i
    i=i+1
print(sum)

# Exercise 3: Print multiplication table of a given number
mul_num=int(input("enter the number"))
i=1
while i<=10:
    mul=i*mul_num
    print(mul)
    i=i+1

# Exercise 4: Count the total number of digits in a number
numbr=int(input("enter the number"))
count=0
while numbr!=0:
    numbr=numbr//10
    count+=1
print(count)

   


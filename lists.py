fruits=["apple","banana","cherry"]
print(fruits[0])
fruits.append("orange")
print(fruits)
numbers=[1,2,3,4,5]
print(numbers[1:4]) 
squares=[x**2 for x in range (5)]
print(squares)
numbrs=[1,9,7,8,5]
numbrs.sort()
print(numbrs)
numbers.reverse()
print(numbers)

a=[11, 11, 13.5,"be10x",True]
print(a)
print(a[2])
print(a[1:4])
print(a[3][4])


fruits.insert(0,"pears")
print(fruits)
a.remove(13.5)
print(a)
fruits.pop(0)
print(fruits)

print(len(fruits))
print(fruits)
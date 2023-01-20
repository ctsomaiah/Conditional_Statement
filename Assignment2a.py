# Assignment - Conditional statements

# 1. Write a Python program to calculate the sum of three given numbers, if the values are less than 100, print value  10,
# else print value  100

print("Enter 1st number")
x1=int(input())
print("Enter 2nd number")
x2=int(input())
print("Enter 3rd number")
x3=int(input())
x = x1 + x2 + x3
if x<100:
    print("Result is 10")
else:
    print("Result is 100")

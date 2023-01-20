# Assignment - Conditional statements

# 4. Write a Python program using conditional statements to check whether a specified value is contained in a group of
#    values
#     Hint:
#         Use 'in'
#     Example : 4 in [12,3,4,5] ---> True

list = [12,3,4,5]
print("Enter the number you want to find")
uIn = int(input())
if uIn in list:
    print("True")
else:
    print("False")

# Assignment - Conditional statements

# 2. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given
# string already begins with "Is" then return the string unchanged

def newStr(list):
    if len(list)>=2 and list[:2]=="Is":
        return list
    return "Is"+list

print(newStr("Something"))
print(newStr("IsNothing"))





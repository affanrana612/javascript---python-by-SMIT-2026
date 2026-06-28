# Variable0 & Data Types
# 1) String
# 2) Integer 
# 3)Boolean
# If conditions
#  ==, <, >, <=, >=
# type casting
# int(), str(), bool()
#  and  elif else
# or  input

# name = input("What is your name? ")
# print("Hello " ,name)

# and both codition should be true
# or any one condition should be true

# marks = int(input("Enter your percentage: ")) 



# if marks > 40 or marks < 60:
#     print("passsssss")
# else:
#     print("fail")

# if :first condition
# elif : creating more than 1 conditions
# else : all conditions are false so it will run

# == equal to
# < less than
# > greater than
# <= less than or equal to
# >= greater than or equal to
# != not equal to


# name1 = ("Abdul Wahhab Rana")
# name2 = ("Abdul Wahhab ")
# if name1 == name2:
#     print("match")
# else:
#     print("not match")

# if andition :
    # code
    
# if 2 > 4:
#     print("true")
# elif 4 > 6:
#     print("yes")
# else:
#     print("helloo")


# 3 input
# 1 input koi bhi num
# 2 input koi bhi 2 num
# 3 add,subtract,multiply,divide,modulus,exponent, floor division,exponent
num1 = int(input("Enter a 1 number: "))
num2 = int(input("Enter a 2 number: "))
operator = input("add,subtract,multiply,divide,modulus,exponent, floor division,exponent: ")
if operator == "add":
    print(num1 + num2)
elif operator == "subtract":
    print(num1 - num2)
elif operator == "multiply":
    print(num1 * num2)
elif operator == "divide":
    print(num1 / num2)
elif operator == "modulus":
    print(num1 % num2)
elif operator == "exponent":
    print(num1 ** num2)
elif operator == "floor division":
    print(num1 // num2)
else:
    print("Invalid operator") 
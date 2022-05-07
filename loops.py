'''
list
set
tuple
dict
loops :- for loop
'''

'''
if elif else :- check


if (condition--> True/False):
    print(msg1)
else:
    print(msg2)


if (condition--> True/False):
    print(msg1)
elif (condition--> True/False)::
    print(msg2) 
.
.
else:
    print(msg..n)

truth table
 or    and

T T  T  T
T F  T  F
F T  T  F
F F  F  F

'''
# name = input("Enter you name:- ")
# age = int(input("Enter you age:- "))
'''
age<18 ...you are not eligible for driving
age=18 .. you can drive with learning license
age>18 .. you can drive
#'''
# if age<18:
#     print("you are not eligible for driving")
# elif age==18:
#     print("you can drive with learning license")
# else:
#     print("you can drive")

'''
num1,num2,num3
num1--->num2 , num3
num2 ---> num1, num3
num3 --> mnum1, num2

'''
# num1,num2,num3 = 15,9,73

# if num1>num2 and num1>num3:
#     print("Num1 is greater", num1)
# elif  num2>num1 and num2>num3:
#     print("Num2 is greater", num2)
# else:
#     print("Num3 is greater", num3)

'''
Write a program to display "Hello" if a number entered by user is a multiple/divisible of five , 
otherwise print "Bye".
'''
# num = int(input("Numb:- "))

# if num%5 == 0:
#     print("Hello")
# else:
#     print("Bye")

'''
Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.

numb = 845

check = numb%10 === 5
if check%3 == 0  ---


Write a program to calculate the electricity bill (accept number of unit from user) 
according to the following criteria :
     Unit                                                            Price  
First 100 units  (0-100)                                            no charge (0rs)
Next 100 units   (101-200)                                           Rs 5 per unit
After 200 units    (201++)                                        Rs 10 per unit
(For example if input unit is 201 then total bill amount is Rs2000)


95unit === 0rs
143unit ===  143-100 = 43 * 5 = 215 
201unit == 201-100 = 101   =  100*5 + 1*10 = 510
'''

# unit = int(input("Enter your units:- "))

# if unit<=100:
#     print("Amount to be pay is 0rs")

# elif unit>100 and unit<201:
#     pay = (unit-100)*5
#     print("Amount to pay is ",pay)
# else:
#     pay = 500+(unit-200)*10
#     print("Amount to pay is ",pay)



'''
Write a program to accept mark from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                         A
         > 80 and <= 90                               B
         >= 60 and <= 80                              C
         below 60                                     D
'''
# marks=int(input("Enter your marks:-"))
# if marks>90:
#     print("Grade A")
# elif marks>80 and marks<=90:
#     print("Grade B")
# elif marks>=60 and marks<=80:
#     print("Grade C")
# else:
#     print("Grade D")

num1, num2 = 10,10
# if num1>num2:
#     print(num1)
# elif num1 == num2:
#     print("equal")
# else:
#     print("B")

# print(num1) if num1>num2 else print("equal") if num1 == num2 else print(num2)

'''
basics --> 1-2 test    1hr ----- 30min
func --- > 2-3 test
oops --- > 1-2 test
final test --> 1-2test
5-9 test

'''

# var1 = "Rohit plays a cricket"
# for i in var1:
#     if i =="s":
#         break
#     print(i)
# var1 = "Rohit"
# for i in var1:
#     if i =="h":
#         continue
#     print(i)
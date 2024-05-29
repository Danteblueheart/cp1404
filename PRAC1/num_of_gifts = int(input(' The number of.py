"""
num_of_gifts = int(input(' The number of students is :'))
num_of_students = int(input("The number of students is ："))

num_of_gift_for_each = num_of_gifts// num_of_students
gift_remained = num_of_gifts % num_of_students
print(f'number of gift for each student is {num_of_gift_for_each}')

print(f'number of gifts remained is {gift_remained}')"""


"""
item_price = float(input('Item price is:'))
GST = 0.09
gst_checking = str(input('yes or no? enter y/n   ')).lower
if gst_checking ==  'y' :
    item_price = item_price + item_price * GST
print(f'${item_price:.2f}')"""
"""
number = int(input('Enter the number:'))

for i in range(1,number+1):
    print(i)
    i += 1
"""
"""
number = int(input('Enter the number:'))
i = 1

while i < number + 1:
    print(i)
    i += 1
    """
"""
NUMBER = 5

guessing_number = int(input("Please guess a number between 1 and 10"))
while guessing_number != NUMBER:
    print("wrong answer,try again!")
    guessing_number = int(input("Please guess a number between 1 and 10"))
print("Yes,the correct answer is{NUMBER}")
"""

"""name = str(input("Please enter your name:")).strip().upper()
while name == "":
    print("cannot be blank")
    name = str(input("Please enter your name:")).strip().upper()
print(f'Your name is : {name}')
salary = float(input("please enter the salary:$"))
while salary < 0:
    print("invalid number")
    salary = float(input("please enter the salary:$"))
print(f'your salary is ${salary:.2f}')
"""
"""
people = int(input("enter the number of ages"))
ages = []

for i in range (people):
    age = int(input("please input an age"))
    ages.append(age)
total = sum(ages)
average = total/ len(ages)
print(total)
print(average)
"""

"""
age = int(input('Please enter your age:'))
total_age = 0
count = 0
average = 0

while age != -1 :
    total_age += age
    count += 1
    average = total_age/count
    age = int(input('Please enter your age:'))
print (f'Total age is {total_age}')
print (f'the average age is {average}')
"""


for i in range (1,4):
    for j in range(2,10,3):
        print(i,"-",j+i)



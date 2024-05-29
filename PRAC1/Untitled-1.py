"""
import random


low = int(input("low number"))
high = int(input("high number"))
while high < low:
    print("error")
    high = int(input("high number"))
n = random.randint(low,high)
print(n * "😊")
"""
"""
def is_even(number):
    return number % 2 == 0
"""
import random
def main():
    names = ['fds','dadsa','dads','dad','dada']
    name = input("enter your name: ")
    while name == "":
        print('error')
        name = input("enter your name: ")
    names.append(name)
    secret = random.choice(names)
    get_valid_name(name)
    print_greetings()
    print_secret_name(secret)

def get_valid_name(name):
    return name

def print_greetings():
    print("greeting-----")

def print_secret_name(a):
    print(f'secret name is:{a}')


main()

    

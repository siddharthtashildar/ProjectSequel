from connection_funcs import *
from misc_funcs import *
import os

print()
print("Welcome To Project Sequel!")
print()
print()
print('How do you want to Login?')
print('1.Manual')
print('2.Using a connection url')
print('3.Defualt LocalHost')
connection_method=input("Enter your choice(1/2/3) or press q to quit: ")
print()

database=''

if connection_method == '1':
    database=connect_Manual()
    print()
    loading_animation()

elif connection_method == '2':
    database=connect_Url()
    print()
    loading_animation()

elif connection_method == '3':
    database=connect_localhost()
    print()
    loading_animation()


print("Welcome to the Party!")
print()

while True:
    ch=input("Project_Sequel> ")

    if ch == 'Quit' or 'q':
        break
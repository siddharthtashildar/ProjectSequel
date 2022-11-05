from connection_funcs import *
from misc_funcs import *
from queries import *
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

#-------LIST TO CHECK QUERIES-------#
create_db_list=[['pls','make', 'database','with','name'],
                ['pls','make', 'db','with','name'],
                ['pls','mk', 'db','with','name'],
                ['pls','mk', 'database','with','name']]

show_db_list=['list databases','ld','list db', 'show databases','list database','show db']


ch=''
quit=['q','Quit','quit','Q']

while ch not in quit  :

    ch=input("Project_Sequel> ")

    if ch.lower().split()[:-1] in create_db_list :
        ex=create_db(database,ch)
        if ex:
            print(f"Successfully created Database named: {ch.split()[5]}")
    
    elif ch.lower() in show_db_list:
        show_db(database)

    
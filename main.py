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
create_db_list=[['make', 'database','with','name'],
                ['make', 'db','with','name'],
                ['mk', 'db','with','name'],
                ['mk', 'database','with','name']]

show_db_list=['list databases','ld','list db', 'show databases','list database','show db']

use_db_list=[['switch','database'],
             ['sw','database'],
             ['sh','database'],
             ['switch','db'],
             ['sw','db'], 
             ['sh','db']]

show_table_list=['list tables','lt','list tbl', 'show tables','list table','show tbl']

ch=''
quit=['q','Quit','quit','Q']
current_db=''
while ch not in quit  :

    ch=input("Project_Sequel> ")

    if ch.lower().split()[:-1] in create_db_list :
        ex=create_db(database,ch)
        if ex:
            print(f"Successfully created Database named: {ch.split()[4]}")
    
    elif ch.lower() in show_db_list:
        print()
        print("The available Database are:")
        num=1
        db_list=show_db(database)
        for i in db_list:
            print(f'{db_list.index(i)+1}) {i}')
            num += 1
        print(f"Total Databases present: {num-1}")
        print()
        
    elif ch.lower().split()[:-1] in use_db_list:
        current_db=use_db(database,ch.split()[2])
        if current_db == ch.split()[2]:
            print(f"Switched to database --> {ch.split()[2]}")
        else:
            print(current_db)
    
    elif ch.lower() in show_table_list:
        print()
        print("The available tables are:")
        num=1
        table_list=show_tables(database,current_db)
        for i in table_list:
            print(f'{table_list.index(i)+1}) {i}')
            num += 1
        print(f"Total Tables present in {current_db}: {num-1}")
        print()
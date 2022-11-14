from connection_funcs import *
from misc_funcs import *
from queries import *
from tabulate import tabulate


print()
print("Welcome To Project Sequel!")
print()
print()
print('How do you want to Login?')
print('1.Manual')
print('2.Using CommandLine Method')
print('3.Defualt LocalHost')
connection_method=input("Enter your choice(1/2/3) or press q to quit: ")
print()

database=''
current_db=''

if connection_method == '1':
    database,current_db=connect_Manual()
    print()
    loading_animation()

elif connection_method == '2':
    database,current_db=connect_cmd()
    print()
    loading_animation()

elif connection_method == '3':
    database,current_db=connect_localhost()
    print()
    loading_animation()



print("Welcome to the Party!")
print()
print("Use 'help' or 'h' to list all commands available! ")
print("Get Started- Use 'ld' to display all database present or use 'make db with name' to create new database!")
print()

#-------LIST TO CHECK QUERIES-------#
quit=['q','Quit','quit','Q']

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

create_table_list=['make table with name',
                   'mk table with name',
                   'make tbl with name',
                   'mk tbl with name']

current_db_list=['curr database','current database','current db','curr db']

desc_table_list=['specifiy' , 'detail', 'define' ,'represent' ,'describe', 'spec', 'dtl', 'def' ,'rep' ,'desc', 'df' ]

drop_db_list=['delete database','remove database','del database','rm database','del db','rm db']

drop_tbl_list=['delete table','remove table','del table','rm table','del tbl','rm tbl']

ch=''

while ch not in quit  :

    ch=input("Project_Sequel> ")

    if ch.lower().split()[:-1] in create_db_list :
        ex=create_db(database,ch)
        if ex:
            print(f"Success--> created Database named: {ch.split()[4]}!")
    
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
            print()
            print(f"Switched to database --> {ch.split()[2]}")
            print()
            print("(use 'switch db' to switch database or use 'lt' to display all tables.')")
            print()

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

    elif check_create_table(ch,create_table_list):
          ex=create_table(database,ch,current_db,ch.split()[4])
          if ex:
            print(f"Success--> Created Table named {ch.split()[4]} in database {current_db}!")
          else:
            print(f' Error--> {ex}')
        
    elif ch.lower() in current_db_list:
        if current_db != '':
            print()
            print(f"You are Currently in: {current_db}")
            print()
            print("(use 'switch db' to switch database or use 'lt' to display all tables.')")
            print()
        else:
            print("You have not selected any Database yet!")
            print()
            print("(use 'switch db' to switch database or use 'mk db with name' to create a new Database)")
            print()

    elif check_desc_table(ch,desc_table_list):
        print()
        data,cols,num=desc_table(database,ch,current_db)
        print(tabulate(data,headers=cols,tablefmt="github"))
        print()
        print(f"Total Columns present in {current_db}: {num}")
        print()
    
    elif ch.lower().startswith('from'):
        
        print()
        data,cols,num=display_data(database,ch,current_db)
        print(tabulate(data,headers=cols,tablefmt="github"))
        print()
        print(f"Total Records present in {current_db}: {num}")
        print()
    
    elif check_drop_db(ch,drop_db_list):
        ex=drop_db(database,ch)
        if ex == True:
            print()
            print(f'Success--> deleted database with name {ch.split()[2]}')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()

    elif check_drop_tbl(ch,drop_tbl_list):
        ex=drop_table(database,ch,current_db)
        if ex == True:
            print()
            print(f'Success--> deleted table with name {ch.split()[2]} from {current_db}!')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()
    
    elif ch.lower().startswith('add data'):
        ex=insert_data(database,ch,current_db)
        if ex == True:
            print()
            tbl=ch.partition('to')[2].partition('(')[0].strip()
            print(f'Success--> Added one row to table {tbl}!')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()

    elif ch.lower().startswith('convert'):
        ex=convertcsv(database,ch,current_db)
        if ex == True:
            print()
            tbl=ch.split()[1].partition('(')[0].strip()
            file=ch.partition('to')[2].partition('with')[0].partition('order by')[0].replace('"','').replace("'",'').strip()
            print(f'Success--> Converted {tbl} to {file}!')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()
    
    elif ch.lower().startswith('rename') or ch.lower().startswith('rn'):
        ex=rename_table(database,ch,current_db)
        if ex == True:
            print()
            old_name=ch.split()[1].strip()
            new_name=ch.split()[3].strip()
            print(f'Success--> Renamed table {old_name} to {new_name}!')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()
    
    elif ch.lower().startswith('add'):
        ex=add_column(database,ch,current_db)
        if ex == True:
            print()
            col_name=ch.split()[1].strip()
            tbl_name=ch.split()[-1:][0].strip()
            print(f'Success--> Added column {col_name} to {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()
    
    elif ch.lower().startswith('modify'):
        ex=modify_column(database,ch,current_db)
        if ex == True:
            print()
            col_name=ch.split()[1].strip()
            tbl_name=ch.split()[-1:][0].strip()
            print(f'Success--> Modified column {col_name} in {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {ex}')
            print()
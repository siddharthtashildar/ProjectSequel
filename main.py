
#------IMPORTING MODULES------#

#User Defined
from connection_funcs import *
from misc_funcs import *
from queries import *
#Libraries
from tabulate import tabulate


#------GLOBAL VARIABLES------#

database=''
current_db=''
quit=['q','Quit','quit','Q']
ch=''

#------CONNECTION SCREEN------#

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

#---Checking Connection Methods---#

if connection_method == '1':
    database,current_db=connect_Manual()
    print()
    if database == '':
        ch = 'quit'
    elif database.is_connected():
        ch = ''
        loading_animation()
        welcome_screen()

elif connection_method == '2':
    database,current_db=connect_cmd()
    print()
    if database == '':
        ch = 'quit'
    elif database.is_connected():
        ch = ''
        loading_animation()
        welcome_screen()

elif connection_method == '3':
    database,current_db=connect_localhost()
    print()
    if database == '':
        ch = 'quit'
    elif database.is_connected():
        ch = ''
        loading_animation()
        welcome_screen()


#------MAIN WHILE LOOP------#


while ch not in quit  :

    ch=input("Project_Sequel> ")

    if check_create_db(ch) :
        ex,err=create_db(database,ch)
        if ex:
            print()
            print(f"Success--> created Database named: {ch.split()[4]}!")
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()

    elif check_show_db(ch):
        print()  
        num=1
        db_list=show_db(database,index=True)
        if db_list != '':
            print("The available Database are:")
            print()
            print(tabulate(db_list, headers=['no','Name'],tablefmt="simple"))
            print()
            print(f"Total Databases present: {len(db_list)}")
            print()
        else:
            print()
            print(f"Total Databases present: {len(db_list)}")
            print()
        
    elif check_use_db(ch):
        db_name=''
        if '-i' in ch.lower().split():
            db_name=show_db(database)[int(ch.split()[3])-1]
        else:
            db_name=ch.split()[2]

        current_db=use_db(database,db_name)

        if current_db == db_name:
            print()
            print(f"Switched to database --> {current_db}")
            print()
            print("(use 'switch db' to switch database or use 'lt' to display all tables.')")
            print()

        else:
            print()
            print(f' Error--> {current_db}')
            print()

    elif check_show_tables(ch):
        print()
        if current_db != '':
            print("The available tables are:")
            print()
            table_list=show_tables(database,current_db,index=True)
            print(tabulate(table_list, headers=['no','Name'],tablefmt="simple"))
            print()
            print(f"Total Tables present in {current_db}: {len(table_list)}")
            print()
        else:
            print("You have not selected any Database yet!")
            print()
            print("(use 'switch db' to switch database or use 'mk db with name' to create a new Database)")
            print()

    elif check_create_table(ch):
          ex,err=create_table(database,ch,current_db,ch.split()[4])
          if ex == True:
            print()
            print(f"Success--> Created Table named {ch.split()[4]} in database {current_db}!")
            print()
          else:
            print()
            print(f' Error--> {err}')
            print()
        
    elif check_current_db(ch):
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

    elif check_desc_table(ch):
        print()
        data,cols,num,tbl_name=desc_table(database,ch,current_db)
        print(tabulate(data,headers=cols,tablefmt="github"))
        print()
        print(f"Total Columns present in {tbl_name}: {num}")
        print()
    
    elif check_display_data(ch):
        print()
        data,cols,num,tbl_name=display_data(database,ch,current_db)
        print(tabulate(data,headers=cols,tablefmt="github"))
        print()
        print(f"Total Records present in {tbl_name}: {num}")
        print()
    
    elif check_drop_db(ch):
        ex,err=drop_db(database,ch)
        if ex == True:
            print()
            print(f'Success--> deleted database with name {ch.split()[2]}')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()

    elif check_drop_tbl(ch):
        ex,err=drop_table(database,ch,current_db)
        if ex == True:
            print()
            print(f'Success--> deleted table with name {ch.split()[2]} from {current_db}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()
    
    elif check_insert_data(ch):
        ex,err=insert_data(database,ch,current_db)
        if ex == True:
            print()
            tbl=ch.partition('to')[2].partition('(')[0].strip()
            print(f'Success--> Added one row to table {tbl}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()

    elif check_convert_csv(ch):
        ex,err=convertcsv(database,ch,current_db)
        if ex == True:
            print()
            tbl=ch.split()[1].partition('(')[0].strip()
            file=ch.partition('to')[2].partition('when')[0].partition('order by')[0].replace('"','').replace("'",'').strip()
            print(f'Success--> Converted {tbl} to {file}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()
    
    elif check_rename_table(ch):
        ex,err=rename_table(database,ch,current_db)
        print('that was really not cool')
        if ex == True:
            print()
            old_name=ch.split()[2].strip()
            new_name=ch.split()[4].strip()
            print(f'Success--> Renamed table {old_name} to {new_name}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()
    
    elif check_add_column(ch):
        ex.err=add_column(database,ch,current_db)
        if ex == True:
            print()
            col_name=ch.split()[1].strip()
            tbl_name=ch.split()[-1:][0].strip()
            print(f'Success--> Added column {col_name} to {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()
    
    elif check_modify_column(ch):
        ex,err=modify_column(database,ch,current_db)
        if ex == True:
            print()
            col_name=ch.split()[1].strip()
            tbl_name=ch.split()[-1:][0].strip()
            print(f'Success--> Modified column {col_name} in {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()

    elif check_delete_column(ch):
        ex,err=delete_column(database,ch,current_db)
        if ex == True:
            print()
            col_name=ch.split()[2].strip()
            tbl_name=ch.split()[4].strip()
            print(f'Success--> Deleted column {col_name} in {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()
    
    elif check_rename_column(ch):
        ex,err=rename_column(database,ch,current_db)
        if ex == True:
            print()
            old_col_name=ch.split()[2].strip()
            new_col_name=ch.partition('to')[2].partition('in table')[0].strip()
            tbl_name=ch.partition('in table')[2].strip()
            print(f'Success--> Renamed column from {old_col_name} to {new_col_name} in {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()
    
    elif check_modify_data(ch):
        ex,rows,err=update_data(database,ch,current_db)
        if ex == True:
            print()
            tbl_name=ch.split()[4].strip()
            print(f'Success--> Modified {rows} rows in {tbl_name}!')
            print()
        else:
            print()
            print(f' Error--> {err}')
            print()

    elif ch == '':
        pass

    elif ch in quit:
        print()   
        Exit_animation()

    else:
        print()
        print('Invalid Input!')
        print()
        print('use "run mysql <your Query> to run mysql query directly (Note: Only runs query and doesnt return anything, so use i=only for modification.)"')
        print()
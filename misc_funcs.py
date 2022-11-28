
#------IMPORT MODULES------#

import time
import sys
import os

#Function for loading screen while connecting to the Database

def loading_animation():
    #String to be displayed when the application is loading
    load_str = "Connection to the server..."
  
    animation = "|/-\\|/-\\|/-\\|/-\\|/-\\"
                          
    for i in range(len(animation)):
        time.sleep(0.075)
        sys.stdout.write("\r"+ load_str+ animation[i])
        sys.stdout.flush()
     
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")

#Function for loading screen while Exiting the program
def Exit_animation():
# String to be displayed when the application is loading
    load_str = "Exiting..."
  
    animation = "|/-\\|/-\\|/-\\|/-\\|/-\\ "
                          
    for i in range(len(animation)):
        time.sleep(0.045)
        sys.stdout.write("\r"+ load_str+ animation[i])
        sys.stdout.flush()

#Welcome Screen After Connecting to The Database
def welcome_screen():
    print("Welcome to the Party!")
    print()
    print("Use 'help' or 'h' to list all commands available! ")
    print("Get Started- Use 'ld' to display all database present or use 'make db with name' to create new database!")
    print()

def check_create_db(ch):
    create_db_list=[['make', 'database','with','name'],
                ['make', 'db','with','name'],
                ['mk', 'db','with','name'],
                ['mk', 'database','with','name']]
    if ch.lower().split()[:-1] in create_db_list:
        return True

def check_show_db(ch):
    show_db_list=['list databases','ld','list db', 'show databases','list database','show db']
    if ch.lower() in show_db_list:
        return True

def check_use_db(ch):
    use_db_list=['switch database',
             'sw database',
             'sh database',
             'switch db',
             'sw db', 
             'sh db']
    for i in use_db_list:
        if ch.lower().startswith(i):
            return True

def check_show_tables(ch):
    show_table_list=['list tables','lt','list tbl', 'show tables','list table','show tbl']
    if ch.lower() in show_table_list:
        return True

def check_create_table(ch):
    create_table_list=['make table with name',
                   'mk table with name',
                   'make tbl with name',
                   'mk tbl with name']
    for i in create_table_list:
        if ch.lower().startswith(i):
            return True

def check_current_db(ch):
    current_db_list=['curr database','current database','current db','curr db']
    if ch.lower() in current_db_list:
        return True

def check_desc_table(ch):
    desc_table_list=['specifiy' , 'detail', 'define' ,'represent' ,'describe', 'spec', 'dtl', 'def' ,'rep' ,'desc', 'df' ]
    for i in desc_table_list:
        if ch.lower().startswith(i):
            return True

def check_display_data(ch):
    if ch.lower().startswith('from'):
        return True

def check_drop_db(ch):
    drop_db_list=['delete database','remove database','del database','rm database','del db','rm db']
    for i in drop_db_list:
        if ch.lower().startswith(i):
            return True

def check_drop_tbl(ch):
    drop_tbl_list=['delete table','remove table','del table','rm table','del tbl','rm tbl']
    for i in drop_tbl_list:
        if ch.lower().startswith(i):
            return True

def check_insert_data(ch):
    if ch.lower().startswith('add data'):
        return True

def check_convert_csv(ch):
    if ch.lower().startswith('convert'):
        return True

def check_rename_table(ch):
    if ch.lower().startswith('rename table'):
        return True

def check_add_column(ch):
    if ch.lower().startswith('add'):
        return True

def check_modify_column(ch):
    if ch.lower().startswith('modify column'):
        return True

def check_delete_column(ch):
    if ch.lower().startswith('delete column'):
        return True

def check_rename_column(ch):
    if ch.lower().startswith('rename column'):
        return True

def check_modify_data(ch):
    if ch.lower().startswith('modify data'):
        return True
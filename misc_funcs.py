import time
import sys
import os


def loading_animation():
# String to be displayed when the application is loading
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

def check_create_table(ch,list):
    for i in list:
        if ch.lower().startswith(i):
            return True

def check_desc_table(ch,list):
    for i in list:
        if ch.lower().startswith(i):
            return True

def check_drop_db(ch,list):
    for i in list:
        if ch.lower().startswith(i):
            return True

def check_drop_tbl(ch,list):
    for i in list:
        if ch.lower().startswith(i):
            return True

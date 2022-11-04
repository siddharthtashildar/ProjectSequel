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

def check_query(ch):
    query_checker=ch.split()

    check_list=[]

    for i in query_checker:
        check_list.append(i.lower())
    return check_list
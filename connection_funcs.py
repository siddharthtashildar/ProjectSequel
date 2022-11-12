
import mysql.connector as mysql
from mysql.connector import errorcode
from urllib.parse import urlparse
import pwinput

def connect_Manual():
    Host=input("Enter Host: ")
    User=input("Enter User: ")
    password = pwinput.pwinput(prompt='Enter Password: ')

    #Host='localhost'
    #User='root'
    #password='pass@123'
    #Database='sample'
    
    # Host='bbvudwhkuqtqhqauukg6-mysql.services.clever-cloud.com'
    # User='uodksj20ljf64ecd'
    # password='KqhImxBuNUQFxIDekwVi'
    # Database='bbvudwhkuqtqhqauukg6'
    db=''
    try:
        db= mysql.connect(host=Host, user=User, password=password)

    except mysql.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        db.close()

    return db

def connect_cmd():
    text = input("Paste your command: ")
    cmd=text.split()
    host=''
    user=''
    port=''
    database=''
    password=''
    for i in cmd:
        if i == '-h':
            host=cmd[cmd.index(i)+1]
        elif i == '-u':
            user=cmd[cmd.index(i)+1]
        elif i == '-P':
            port=cmd[cmd.index(i)+1]
        elif i == '-D':
            database=cmd[cmd.index(i)+1]
        elif i.startswith('-p') and len(i) > 2:
            password=i[2:]
        elif i == '-p':
            password = pwinput.pwinput(prompt='Enter your Password: ')
    
    try:
        db= mysql.connect(host=host, user=user, password=password)

    except mysql.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        db.close()

    return db

def connect_localhost():
    Host='localhost'
    User='root'
    #password = pwinput.pwinput(prompt='Enter your Localhost Password: ')
    password='blackpearl'
    db=''
    try:
        db= mysql.connect(host=Host, user=User, password=password)

    except mysql.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        db.close()

    return db
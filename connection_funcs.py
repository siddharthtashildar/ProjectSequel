
import mysql.connector as mysql
from mysql.connector import errorcode
from urllib.parse import urlparse
import pwinput

def connect_Manual():
    Host=input("Enter Host: ")
    User=input("Enter User: ")
    password = pwinput.pwinput(prompt='Enter Password: ')
    Database=input("Enter Database(optional): ")

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
        if Database == '' :
            db= mysql.connect(host=Host, user=User, password=password)
        else:
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

def connect_Url():
    url = input("Paste your url: ")
    result = urlparse(url)
    mysql.connect(host=result.hostname,user=result.username,passwd=result.password)

def connect_localhost():
    Host='localhost'
    User='root'
    #password = pwinput.pwinput(prompt='Enter your Localhost Password: ')
    password='blackpearl'
    Database=input("Enter Database name(optional hit enter to skip and connect): ")
    db=''
    try:
        if Database == '' :
            db= mysql.connect(host=Host, user=User, password=password)
        else:
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
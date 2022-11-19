
import mysql.connector as mysql
from mysql.connector import errorcode
import pwinput

def connect_Manual():
    Host=input("Enter Host: ")
    User=input("Enter User: ")
    password = pwinput.pwinput(prompt='Enter Password: ')
    Database=input('Enter Database(optional): ')

    #Host='localhost'
    #User='root'
    #password='pass@123'
    #Database='sample'
    
    # Host='bbvudwhkuqtqhqauukg6-mysql.services.clever-cloud.com'
    # User='uodksj20ljf64ecd'
    # password='KqhImxBuNUQFxIDekwVi'
    # Database='bbvudwhkuqtqhqauukg6'
    db=''
    if len(Database)==0:
        try:
            
            db= mysql.connect(host=Host, user=User, password=password)
            return db,Database

        except mysql.Error as err:
            print()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            db.close()
    else:       
        try:
            
            db= mysql.connect(host=Host, user=User, password=password,database=Database)
            return db,Database

        except mysql.Error as err:
            print()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            db.close()

    return db,''

def connect_cmd():
    print('Example: mysql -h YourHost -u YourUser -pYourPassword -P yourPort(optional) -D databaseName(optional)')
    text = input("Paste your command: ")
    cmd=text.split()
    Host='localhost'
    User=''
    Port=3306
    Database=''
    password=''
    db=''
    for i in cmd:
        if i == '-h':
            if cmd[cmd.index(i)+1] != Host :
                Host=cmd[cmd.index(i)+1]
            
        elif i == '-u':
            User=cmd[cmd.index(i)+1]

        elif i == '-P':
            if cmd[cmd.index(i)+1] != Port:
                Port=cmd[cmd.index(i)+1]

        elif i == '-D':
            Database=cmd[cmd.index(i)+1]

        elif i.startswith('-p') and len(i) > 2:
            password=i[2:]
            
        elif i == '-p':
            password = pwinput.pwinput(prompt='Enter your Password: ')

    if len(Database)==0:
        try:
            
            db= mysql.connect(host=Host, user=User, password=password)
            return db,Database

        except mysql.Error as err:
            print()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            db.close()
    else:       
        try:
            
            db= mysql.connect(host=Host, user=User, password=password,database=Database)
            return db,Database

        except mysql.Error as err:
            print()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            db.close()

    return db,''

def connect_localhost():
    Host='localhost'
    User='root'
    password = pwinput.pwinput(prompt='Enter your Localhost Password: ')
    Database=input('Enter Database (Optional): ')
    db=''

    if len(Database)==0:
        try:
            
            db= mysql.connect(host=Host, user=User, password=password)
            return db,Database

        except mysql.Error as err:
            print()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            db.close()
    else:       
        try:
            
            db= mysql.connect(host=Host, user=User, password=password,database=Database)
            return db,Database

        except mysql.Error as err:
            print()
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            db.close()

    return db,''
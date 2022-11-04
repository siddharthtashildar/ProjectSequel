# #IMPORTS
# import mysql.connector as mysql1
# import csv

# def connect_db():
#     Host=input("Enter Host: ")
#     User=input("Enter User: ")
#     password=input("Enter Password: ")
#     Database=input("Enter Database: ")

#     #Host='localhost'
#     #User='root'
#     #password='pass@123'
#     #Database='sample'
    
#     # Host='bbvudwhkuqtqhqauukg6-mysql.services.clever-cloud.com'
#     # User='uodksj20ljf64ecd'
#     # password='KqhImxBuNUQFxIDekwVi'
#     # Database='bbvudwhkuqtqhqauukg6'
    
#     db= mysql1.connect(host=Host, user=User, password=password, database=Database)
#     return db

# def get_table_names(db):
#     dbcursor=db.cursor()
#     dbcursor.execute("Show tables")
#     table=dbcursor.fetchall()
#     Num=1
#     print("The Tables available in Database are:")
#     for i in table:
#         for j in i:
#             dude=str(Num) + ") " + j
#             print(dude)
#             Num+=1

# def fetch_data(db,table):
#     dbcursor=db.cursor()
#     query=f"SELECT * FROM {table}"
#     dbcursor.execute(query)
#     data=dbcursor.fetchall()
#     col=dbcursor.column_names
#     list=[]
#     list.append(col)

#     for x in data:
#         list.append(x)

#     db.close()

#     return list

# def tocsv(file,mode,list):
#     filepath=f"{file}.csv"
#     filehandle=open(filepath,mode)
#     writer=csv.writer(filehandle)
#     for y in list:
#         writer.writerow(y)
#     filehandle.close()
#     return True


# a=connect_db()

# get_table_names(a)

# table=input("Enter Your table Name: ")

# data=fetch_data(a,table)

# print("Do you want to create a new csv file or append in existing?")
# print('1. new')
# print('2. append')

# ch=input("Enter your choice: ")

# if ch == 'new':
#     filename=input("Enter your desired csv file name and path to save it(path is optional): ")
#     a=tocsv(filename,'w+',data)
#     if a:
#         print("Successfully Converted!")

# if ch=='append':
#     filename=input("Enter file path and name: ")
#     tocsv(filename,'a+',data)
#     if a:
#         print("Successfully Converted!")

text=input("Enter: ")

if text == '':
    print(text)
    print("This works!")
else:
    print("This doesnt work!")


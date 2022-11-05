import mysql.connector 

def create_db(db,user_query):
    db.reconnect()
    db_name=''
    user_query=user_query.split()
    for i in user_query:
        if i.lower() == 'name':
            db_name = user_query[user_query.index(i) + 1 ]


    query=f"create database {db_name}"

    dbcursor = db.cursor()
    dbcursor.execute(query)
    return True

def show_db(db):
    db.reconnect()
    dbcursor=db.cursor()
    dbcursor.execute("Show databases")
    table=dbcursor.fetchall()
    Num=1
    print()
    print("The available Database are:")
    for i in table:
        for j in i:
            dude=str(Num) + ") " + j
            print(dude)
            Num+=1
    print(f"Total databases present: {Num-1}")
    print()
    return
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
    list=[]

    for i in table:
        for j in i:
            list.append(j)

    return list

def use_db(db,db_name):
    db.reconnect()
    if db_name in show_db(db):
        dbcursor=db.cursor()
        dbcursor.execute(f"use {db_name}")
        return db_name
    else:
        return f"Database named: {db_name} doesnt exist!"

def show_tables(db,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    dbcursor=db.cursor()
    dbcursor.execute("Show tables")
    table=dbcursor.fetchall()
    list=[]
    for i in table:
        for j in i:
            list.append(j)
            
    return list

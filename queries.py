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

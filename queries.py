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
    db.commit()
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
        db.commit()
        return db_name
    else:
        return f"Database named: {db_name} doesnt exist!"

def show_tables(db,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    if dbname == db_name:
        dbcursor=db.cursor()
        dbcursor.execute("Show tables")
        table=dbcursor.fetchall()
        list=[]
        for i in table:
            for j in i:
                list.append(j)
        return list
    else:
        print(dbname)

def create_table(db,query,db_name,table_name):
    user_query=query.partition(table_name)
    db.reconnect()
    dbname=use_db(db,db_name)
    if dbname == db_name:
        dbcursor=db.cursor()
        dbcursor.execute(f"create table {table_name} {user_query[2]}")
        db.commit()
        return True
    else:
        return dbname

def desc_table(db,query,db_name):
    db.reconnect()
    tbl_name=query.split()[1]
    dbname=use_db(db,db_name)
    if tbl_name in show_tables(db,db_name):
        dbcursor=db.cursor()
        dbcursor.execute(f'desc {tbl_name}')
        col=dbcursor.description
        data=dbcursor.fetchall()
        clist=[]
        for x in col:
            clist.append(x[0])

        for i in data:
            print(f'{clist[0]} --> {i[0]}')
            print(f'{clist[1]} --> {i[1]}')
            print(f'{clist[2]} --> {i[2]}')
            print(f'{clist[3]} --> {i[3]}')
            print(f'{clist[4]} --> {i[4]}')
            print(f'{clist[5]} --> {i[5]}')
            print()
        print()
        print(f"Total Columns present in {tbl_name}: {len(data)}")
        print()
    else:
        print(f'No table named {tbl_name} prensent in {db_name}')

def display_data(db,query,db_name):
    db.reconnect()
    tbl_name=query.split()[1]
    dbname=use_db(db,db_name)
    user_query=query.lower().split()
    column=query.partition('display')[2].partition('with')[0]
    clauses=query.partition('with')[2]
    list=[]
    if tbl_name in show_tables(db,db_name):
        dbcursor=db.cursor()
        if 'with' in user_query:
            dbcursor.execute(f"select {column} from {tbl_name} where {clauses}")
            table=dbcursor.fetchall()
            for i in table:
                list.append(i)
            return list
        else:
            order=['order','by']
            if order in user_query:
                dbcursor.execute(f"select {column} from {tbl_name} order by {query.partition('order by')[2]}")
                table=dbcursor.fetchall()
                for i in table:
                    list.append(i)
                return list
            else:
                dbcursor.execute(f"select {column} from {tbl_name}")
                table=dbcursor.fetchall()
                for i in table:
                    list.append(i)
                return list
    else:
        print(f"No Table named {tbl_name} present in {db_name}")   
        

        
            


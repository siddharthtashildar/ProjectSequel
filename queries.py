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
        return f"Database named {db_name} doesnt exist!"

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
    num=0
    dlist=[]
    if tbl_name in show_tables(db,db_name):
        dbcursor=db.cursor()
        dbcursor.execute(f'desc {tbl_name}')
        col=dbcursor.column_names
        data=dbcursor.fetchall()
        for i in data:
            rec=list(i)
            rec[1]=rec[1].decode()
            dlist.append(rec)
            num += 1
        return dlist,col,num


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
    col=''
    num=0
    if tbl_name in show_tables(db,db_name):
        dbcursor=db.cursor()
        if 'with' in user_query:
            dbcursor.execute(f"select {column} from {tbl_name} where {clauses}")
            col=dbcursor.column_names
            table=dbcursor.fetchall()
            for i in table:
                list.append(i)
                num += 1
            return list,col,num
        else:
            order=['order','by']
            if order in user_query:
                dbcursor.execute(f"select {column} from {tbl_name} order by {query.partition('order by')[2]}")
                col=dbcursor.column_names
                table=dbcursor.fetchall()
                for i in table:
                    list.append(i)
                    num += 1
                return list,col,num
            else:
                dbcursor.execute(f"select {column} from {tbl_name}")
                col=dbcursor.column_names
                table=dbcursor.fetchall()
                for i in table:
                    list.append(i)
                    num += 1
                return list,col,num
    else:
        print(f"No Table named {tbl_name} present in {db_name}")   
        

def drop_db(db,query):
    db.reconnect()
    db_name=query.split()[2]
    if db_name in show_db(db):
        dbcursor=db.cursor()
        dbcursor.execute(f"drop database {db_name}")
        db.commit()
        return True
    else:
        return f'No database name {db_name} present!'

            
def drop_table(db,query,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    tbl_name=query.split()[2]
    if dbname == db_name:
        if tbl_name in show_tables(db,db_name):
            dbcursor=db.cursor()
            dbcursor.execute(f"drop table {tbl_name}")
            db.commit()
            return True
        else:
            return f'No table with name {tbl_name} present in {db_name}!'
    else:
        return 'No database seleted!'

def insert_data(db,query,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    tbl_name=query.partition('to')[2].partition('(')[0].strip()
    values=query.partition('to')[0].partition('data')[2].strip()
    cols=query.partition(tbl_name)[2].strip()
    if dbname == db_name:
        if tbl_name in show_tables(db,db_name):
            dbcursor=db.cursor()
            dbcursor.execute(f"insert into {tbl_name}{cols} values{values}")
            db.commit()
            return True
        else:
            return f'No table with name {tbl_name} present in {db_name}!'
    else:
        return 'No database seleted!'

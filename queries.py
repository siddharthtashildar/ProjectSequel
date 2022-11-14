import mysql.connector 
import csv 

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
        dbcursor.execute(f"create table {table_name} {user_query[2].strip()}")
        db.commit()
        return True
    else:
        return dbname

def desc_table(db,query,db_name):
    db.reconnect()
    tbl_name=query.split()[1].strip()
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
    tbl_name=query.split()[1].strip()
    dbname=use_db(db,db_name)
    user_query=query.lower().split()
    column=query.partition('display')[2].partition('with')[0].strip()
    clauses=query.partition('with')[2].strip()
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
            if 'order by' in query.lower():
                dbcursor.execute(f"select {column} from {tbl_name} order by {query.partition('order by')[2].strip()}")
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
    db_name=query.split()[2].strip()
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
    tbl_name=query.split()[2].strip()
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

def convertcsv(db,query,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    tbl_name=query.split()[1].partition('(')[0].strip()
    file_name=query.partition('to')[2].partition('with')[0].partition('order by')[0].replace('"','').replace("'",'').strip()
    cols=query.partition('to')[0].partition(tbl_name)[2].replace('(','').replace(')','').strip()
    clauses=query.partition('with')[2].strip()
    if len(cols) == 0:
        cols='*'
    if dbname == db_name:
        if tbl_name in show_tables(db,db_name):
            dbcursor=db.cursor()
            if 'with' in query.lower().split():
                dbcursor.execute(f"select {cols} from {tbl_name} where {clauses}")
                col=dbcursor.column_names
                table=dbcursor.fetchall()
                try:
                    filehandle=open(file_name,'w')
                    writer=csv.writer(filehandle)
                    writer.writerow(col)
                    for y in table:
                        writer.writerow(y)
                    filehandle.close()
                    return True
                except:
                    return 'Something went wrong!'
            else:
                if 'order by' in query.lower():
                    dbcursor.execute(f"SELECT {cols} FROM {tbl_name} ORDER BY {query.partition('order by')[2].strip()}")
                    col=dbcursor.column_names
                    table=dbcursor.fetchall()
                    try:
                        filehandle=open(file_name,'w')
                        writer=csv.writer(filehandle)
                        writer.writerow(col)
                        for y in table:
                            writer.writerow(y)
                        filehandle.close()
                        return True
                    except:
                        return 'Something went wrong!'

                else:
                    dbcursor.execute(f"select {cols} from {tbl_name}")
                    col=dbcursor.column_names
                    table=dbcursor.fetchall()
                    try:
                        filehandle=open(file_name,'w')
                        writer=csv.writer(filehandle)
                        writer.writerow(col)
                        for y in table:
                            writer.writerow(y)
                        filehandle.close()
                        return True
                    except:
                        return 'Something went wrong!'
        else:
            return f'No table with name {tbl_name} present in {db_name}!'
    else:
        return 'No database seleted!'

def rename_table(db,query,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    old_name=query.split()[1].strip()
    new_name=query.split()[3].strip()
    if dbname == db_name:
        if old_name in show_tables(db,db_name):
            dbcursor=db.cursor()
            dbcursor.execute(f"alter table {old_name} rename to {new_name}")
            db.commit()
            return True
        else:
            return f'No table with name {old_name} present in {db_name}!'
    else:
        return 'No database seleted!'

def add_column(db,query,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    col_name=query.split()[1].strip()
    tbl_name=query.split()[-1:][0].strip()
    definations=query.partition(col_name)[2].partition(f'to table')[0].strip()
    if dbname == db_name:
        if tbl_name in show_tables(db,db_name):
            dbcursor=db.cursor()
            dbcursor.execute(f"alter table {tbl_name} add {col_name} {definations}")
            db.commit()
            return True
        else:
            return f'No table with name {tbl_name} present in {db_name}!'
    else:
        return 'No database seleted!'

def modify_column(db,query,db_name):
    db.reconnect()
    dbname=use_db(db,db_name)
    col_name=query.partition('in table')[0].partition('modify')[2].strip()
    tbl_name=query.split()[-1:][0].strip()
    if dbname == db_name:
        if tbl_name in show_tables(db,db_name):
            dbcursor=db.cursor()
            dbcursor.execute(f"alter table {tbl_name} modify {col_name}")
            db.commit()
            return True
        else:
            return f'No table with name {tbl_name} present in {db_name}!'
    else:
        return 'No database seleted!'
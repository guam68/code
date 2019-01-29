from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import credentials


# Creates a new database 'testdb'
def create_db():
    con = None
    con = connect(database='postgres', user='test', host = 'localhost', password='test')

    dbname = 'testdb'

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute('CREATE DATABASE ' + dbname)
    cur.close()
    con.close()


# Add a table to 'testdb'
def add_table():
    con = None
    con = connect(dbname='testdb', user='test', host = 'localhost', password='test')

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute("""
        create table test_table(
            id serial primary key not null,
            name text not null,
            age int not null
        );
        """)
    cur.close()
    con.close()


# Insert data into table. Takes a tuple (name, age). Id of table is generated automatically through serial type
def add_tester(tester):
    con = None
    con = connect(dbname='testdb', user='test', host='localhost', password='test')

    #   %s is used by psycopg2. Do NOT use % for string formating due to sql injection attack vulnerability
    sql = """
        insert into test_table(name, age) values(%s, %s);       
    """

    name, age = tester

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    cur.execute(sql, (name, age))
    cur.close()
    con.close()


# Get info from table. Also utilizes dict from credentials.py to authenticate user
def get_tester():
    con = None
    con = connect(dbname='testdb', user=credentials.login['user'], host='localhost', password=credentials.login['password'])

    sql = """
        select * from test_table;       
    """
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()

    cur.execute(sql)
    data = cur.fetchall()

    cur.close()
    con.close()
    return data





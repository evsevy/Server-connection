import pymssql 
import argparse
import sqlite3
import pandas as pd

conn = pymssql.connect(server='103.24.99.76', 
                        user='testUser', 
                        password='Abcd.1234', 
                        database='Portal_Data')

def get_sql():
    cursor = conn.cursor()
    cursor.execute("""SELECT *
                FROM sys.databases 
                WHERE name='Portal_Data' 
                """)                
    for row in cursor.fetchall(): 
        #print ('{}'.format(row[0]))
        print("%s\n" % str(row)) 
raww = get_sql()
conn.close()

#cursor = conn.cursor()
    #cursor.execute("""SELECT PARSE(name, database_id, create_date
                #FROM sys.databases) AS Result""")
    #cursor.execute("EXEC sp_databases")
    #cursor.execute("SELECT name FROM master.dbo.sysdatabases")
    #cursor.execute("""SELECT name, database_id, create_date
                #FROM sys.databases 
                #WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb') 
                #""")                
    #for row in cursor.fetchall(): 
        #print ('{}'.format(row[0]))
        #print("%s\n" % str(row)) 

import sqlite3
import csv
import os

def create_db_table():
    conn = sqlite3.connect('DATABASE.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS Portal_Data 
             (Portal_Data)''')           
			
    conn.commit()
    conn.close()

def import_one_file_csv_to_sqlite():
    con = sqlite3.connect('DATABASE.db')
    cur = con.cursor()

    with open('C:\\Users\\AllOneNeon\\Python\\data.csv', 'r', encoding='utf-8') as open_csv:
        rows = csv.reader(open_csv, delimiter="|")
        
        for row in rows:
            cur.execute('INSERT INTO Portal_Data VALUES (?)', row)

    con.commit()
    con.close()  
                
if __name__ == '__main__':
    create_db_table()
    import_one_file_csv_to_sqlite()

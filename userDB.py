#!/usr/bin/python
#创建表
import sqlite3

def searchDB(db_name = "user.db",tb_name = "user"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    query = "select name,password from %s;"%tb_name
    name,password = cursor.execute(query).fetchone()
    conn.close()
    return name,password

# searchDB(db_name = "user.db",tb_name = "user")
if __name__ == "__main__":
    name, password = searchDB(db_name = "user.db",tb_name = "user")
    print(name,password)
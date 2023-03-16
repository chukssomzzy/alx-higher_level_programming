#!/usr/bin/python3

"Select states with python from mysql database"
import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

conn = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password,
                db=db_name, charset="utf8")
cur = conn.cursor()
cur.execute(""" SELECT * FROM db_name
            ORDER BY id """)

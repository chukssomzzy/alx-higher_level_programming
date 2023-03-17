#!/usr/bin/python3

"""lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    with conn.cursor() as cur:
        cur.execute("""SELECT t2.name
                    FROM states AS t1 INNER JOIN cities AS t2
                    ON t2.state_id = t1.id
                    WHERE t1.name = %s;""", (sys.argv[4],))
        rows = cur.fetchall()
        for i in range(len(rows)):
            print(f"{(rows[i][0])}", sep='', end="")
            if i < (len(rows) - 1):
                print(", ", end="")
        print()
    conn.close()

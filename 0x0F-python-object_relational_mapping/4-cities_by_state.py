#!/usr/bin/python3

"""List all cities from the database
`hbtn_0e_0_usa`
"""
import sys
import MySQLdb

if __name__ == '__main__':
    with MySQLdb.connect(host="localhost", passwd=sys.argv[2], port=3306,
                         user=sys.argv[1], db=sys.argv[3]) as conn:
        with conn.cursor() as cur:
            cur.execute("""SELECT cities.id, cities.name, states.name
                            FROM
                                states
                            INNER JOIN
                                cities
                            ON
                                (states.id = cities.state_id)
                            ORDER BY
                                cities.id ASC
                        """)
            cities = cur.fetchall()
            for city in cities:
                print(city)

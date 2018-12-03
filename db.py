import sys
import os
import sqlite3
from contextlib import closing

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "/Users/keegan_sadowski/PycharmProjects/untitled10/shoppingcartdb.sqlite"
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row



    cur = conn.cursor()
    cur.execute('SELECT id, cost FROM item')

    rows = cur.fetchall()

    #id, cost = rows['id'], rows['cost']

    #print(id, cost)TypeError: list indices must be integers or slices, not str


def close():
    if conn:
        conn.close()



connect()

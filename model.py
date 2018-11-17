import sqlite3
from pkg_resources._vendor.pyparsing import empty
#import os.path


def read_halbzeug(material):
    sql = "SELECT * FROM halbzeug WHERE material = " + material
    cursor.execute(sql)
    return cursor

def read_all_materials():
    sql = "SELECT * FROM material"
    cursor.execute(sql)
    return cursor

def read_all_machines():
    sql = "SELECT * FROM maschine"
    cursor.execute(sql)
    return cursor

connection = sqlite3.connect("PoC.db")
cursor = connection.cursor()

"""
sql = "SELECT * FROM material"

cursor.execute(sql)

for dsatz in cursor:
    i = 0
    result = ""
    while i < len(dsatz):
        if result == "":
            result = str(dsatz[i])
        else:
            result = result + ";" + str(dsatz[i])
        i += 1
    print(result)

sql = "SELECT * FROM halbzeug"

cursor.execute(sql)

for dsatz in cursor:
    i = 0
    result = ""
    while i < len(dsatz):
        if result == "":
            result = str(dsatz[i])
        else:
            result = result + ";" + str(dsatz[i])
        i += 1
    print(result)

sql = "SELECT * FROM maschine"

cursor.execute(sql)

for dsatz in cursor:
    i = 0
    result = ""
    while i < len(dsatz):
        if result == "":
            result = str(dsatz[i])
        else:
            result = result + ";" + str(dsatz[i])
        i += 1
    print(result)

sql = "SELECT * FROM werkzeug"

cursor.execute(sql)

for dsatz in cursor:
    i = 0
    result = ""
    while i < len(dsatz):
        if result == "":
            result = str(dsatz[i])
        else:
            result = result + ";" + str(dsatz[i])
        i += 1
    print(result)
"""

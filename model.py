import sqlite3
from pkg_resources._vendor.pyparsing import empty
#import os.path


def read_halbzeug(material):
    sql = "SELECT * FROM halbzeug WHERE material = " + material +" ORDER BY volumen"
    cursor.execute(sql)

    resultSet = []

    for dataset in cursor:
        resultDict = dict()
        resultDict['id'] = dataset[0]
        resultDict['material'] = dataset[1]
        resultDict['a'] = dataset[2]
        resultDict['b'] = dataset[3]
        resultDict['c'] = dataset[4]
        resultDict['stange'] = dataset[5]
        resultDict['volumen'] = dataset[6]
        resultSet.append(resultDict)

    return resultSet

def read_all_materials():
    sql = "SELECT * FROM material"
    cursor.execute(sql)

    resultSet = []

    for dataset in cursor:
        resultDict = dict()
        resultDict['material'] = dataset[0]
        resultDict['normbez'] = dataset[1]
        resultDict['chembez'] = dataset[2]
        resultDict['dichte'] = dataset[3]
        resultDict['preis'] = dataset[4]
        resultSet.append(resultDict)

    return resultSet

def read_all_machines():
    sql = "SELECT * FROM maschine"
    cursor.execute(sql)

    resultSet = []

    for dataset in cursor:
        resultDict = dict()
        resultDict['id'] = dataset[0]
        resultDict['bez'] = dataset[1]
        resultDict['achsen'] = dataset[2]
        resultDict['mss'] = dataset[3]
        resultDict['ruest'] = dataset[4]
        resultSet.append(resultDict)

    return resultSet

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

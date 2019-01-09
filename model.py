import sqlite3
import utils

def read_halbzeug(material):
    sql = "SELECT * FROM halbzeug WHERE material = ?" + " ORDER BY volumen"
    cursor.execute(sql, (material,))

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

def update_halbzeug(material,halbzeug):
    sql = ''' DELETE
              FROM halbzeug
                 WHERE
                 material = ?'''
    cursor.execute(sql, material)

    sql = "INSERT INTO halbzeug (id, material, a, b, c, stange, volumen) VALUES (?,?,?,?,?,?,?)"
    for item in halbzeug:
        cursor.execute(sql, item)

    connection.commit()

def read_all_materials():
    sql = "SELECT * FROM material"
    cursor.execute(sql)

    resultSet = []

    for dataset in cursor:
        resultDict = utils.build_material_dict(dataset)
        resultSet.append(resultDict)

    return resultSet

def read_all_machines():
    sql = "SELECT * FROM maschine"
    cursor.execute(sql)

    resultSet = []

    for dataset in cursor:
        resultDict = utils.build_machine_dict(dataset)
        resultSet.append(resultDict)

    return resultSet

def read_machine(id):
    sql = "SELECT * FROM maschine WHERE id = ?"
    cursor.execute(sql, id)

    resultSet = []

    for dataset in cursor:
        machineData = utils.build_machine_dict(dataset)

    return machineData

def update_material(material):
    sql = ''' UPDATE material
              SET normbez = ? ,
                  chembez = ? ,
                  dichte = ?,
                  preis = ?
              WHERE material = ?'''
    cursor.execute(sql, material)
    connection.commit()

def delete_material(material):
    sql = ''' DELETE
              FROM material
                 WHERE
                 material = ?'''
    cursor.execute(sql, material)
    connection.commit()

def insert_material(material):
    sql = "INSERT INTO material (material, normbez, chembez, dichte, preis) VALUES (?,?,?,?,?)"
    cursor.execute(sql, material)
    connection.commit()

def read_material(material):
    sql = "SELECT * FROM material WHERE material = ?"
    cursor.execute(sql, (material,))

    for dataset in cursor:
        materialData = utils.build_material_dict(dataset)

    return materialData

def setSfg(data):
    global sfg
    sfg = data

def getSfg():
    global sfg
    return sfg

def initSfg():
    global sfg
    sfg = []

def setPockets(data):
    global pockets
    pockets = data

def getPockets():
    global pockets
    return pockets

def initPockets():
    global pockets
    pockets = []

def initVolumeScaling():
    global volumeScaling
    volumeScaling = []

def setVolumeScaling(data):
    global volumeScaling
    volumeScaling = data

def getVolumeScaling():
    global volumeScaling
    return volumeScaling

def initRuntimeVariables():
    initSfg()
    initPockets()
    initVolumeScaling()

connection = sqlite3.connect("PoC.db")
cursor = connection.cursor()

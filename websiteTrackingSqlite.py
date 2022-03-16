import sqlite3
import datetime
from psutil import users

dbName = 'websiteTracking.db'

def openConnection(dbName):
    con = sqlite3.connect(dbName)
    cur = con.cursor()
    print(f'Opened DB Connection with {dbName}')
    return (con, cur)

def closeConnection(con, cur):
    con.close()
    print(f'Closed {dbName} DB connection')


def createTables(con, cur):
    cur.execute('''CREATE TABLE IF NOT EXISTS websites
                    (url str, time timestamp, hash str)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS users
                    (username str)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS websites_users
                    (website_id int, username_id int, active int)''')
    cur.execute('''CREATE TABLE IF NOT EXISTS tracking_timeout
                    (websites_users_id int, timeout int)''')
    con.commit()

def populateTablesWithDummyData(con, cur):
    now = datetime.datetime.now()
    cur.execute('''INSERT INTO websites VALUES ('www.google.com', ?, 'testHash')''', (now,))
    cur.execute("INSERT INTO users VALUES ('pwndcube')")
    websites_id=1
    users_id=1
    websites_users_insert = [websites_id, users_id]
    cur.execute("INSERT INTO websites_users VALUES (?, ?, 1)", websites_users_insert)
    websites_users_id = 1
    cycleTimeout = 7
    tracking_timeout_insert = [websites_users_id, cycleTimeout]
    cur.execute("INSERT INTO tracking_timeout VALUES (?, ?)", tracking_timeout_insert)
    con.commit()

def queryTableRows(con, cur, colName, tableName):
    cur.execute(f"SELECT {colName} FROM {tableName}")    
    fetchTuple = cur.fetchall()
    return fetchTuple

(con, cur) = openConnection(dbName)

print(queryTableRows(con, cur, 'url', 'websites'))

closeConnection(con, cur)

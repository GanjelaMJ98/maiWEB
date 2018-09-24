import sqlite3


conn = sqlite3.connect('Test_DB.sqlite')
cursor = conn.cursor()

def pr(list):
    print("Name = " ,list[0][0])

def sel(name):
    sql = "SELECT * FROM book WHERE name = ?"
    cursor.execute(sql,[(name)])
    #print(cursor.fetchall())
    pr(cursor.fetchall())


#read
print("Listing:")
for row in cursor.execute("SELECT * from book ORDER BY name"):
    print(row)

sel('Kate')













conn.close()
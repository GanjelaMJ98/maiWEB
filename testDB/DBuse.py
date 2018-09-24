import sqlite3
conn = sqlite3.connect('Test_DB.sqlite')
cursor = conn.cursor()
#create
cursor.execute("""INSERT INTO book
                    VALUES('Pavel','89017014147','Mai')
    """)
conn.commit()
book = [('Artem',"89033128577","Mai"),
        ("Kate", "89533128500","Kgu"),
        ("Vlad", "88005553535","Mai")]
cursor.executemany("INSERT INTO book VALUES(?,?,?)",book)
conn.commit()
















conn.close()
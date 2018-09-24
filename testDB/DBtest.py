import sqlite3
conn = sqlite3.connect('PhoneBook.sqlite')
cursor = conn.cursor()
#create
cursor.execute("""CREATE TABLE book
                    (name text, lastname text, num text,adress text, work text)
                """)



conn.close()
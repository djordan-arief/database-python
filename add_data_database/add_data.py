import sqlite3
connection_mem = sqlite3.connect('python project/add_data_database/database.db')
cr = connection_mem.cursor()

# cr.execute("""CREATE TABLE user_data (
#     first_name text,
#     last_name text,
#     password text
# )""")

cr.execute("SELECT * FROM user_data")
record = cr.fetchall()
for i in record:
    print(i)

connection_mem.commit()
connection_mem.close()
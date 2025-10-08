import sqlite3

connection=sqlite3.connect("sqlite.db")
cursor=connection.cursor()

# 1. create a table
cursor.execute(
    """CREATE TABLE IF NOT EXISTS shipment (
    id INTEGER PRIMARY KEY,
    content TEXT,
    weight REAL,
    status TEXT
    )"""
)

# cursor.execute("DROP TABLE shipment")
# connection.commit()

# 2. Add Shipment Data

# cursor.execute("""
#     INSERT INTO shipment(id,content,weight,status)
#     VALUES(12701, 'metal gears',12.7, 'in_transit')    
# """)

# connection.commit()

# 3. Read a shipemnt by id 
# cursor.execute("""
# SELECT * FROM shipment WHERE id=12702
#  """)

# result=cursor.fetchmany(2)
# print(result)

# 4. update shipment

cursor.execute("""
UPDATE shipment SET status = 'in_transit'
               WHERE id=12701""")

connection.commit()


#5. delete a shipment by id
# cursor.execute("""
# DELETE FROM shipment
# WHERE id=12703""")
# connection.commit()
connection.close()


import psycopg2
conn = psycopg2.connect(database="mydb", user='postgres', password='password', host='127.0.0.1', port= '5432')
conn.autocommit = True
cursor = conn.cursor()

cursor.execute('''INSERT INTO kafkaadmin(topic) VALUES ('Ramya')''')
conn.commit()
print("Records inserted........")


conn.close()
import psycopg2
postgresConnection    = psycopg2.connect("dbname=test user=test password='test'")
cursor                = postgresConnection.cursor()
name_Table            = "topicsname"
sqlCreateTable = "CREATE TABLE "+name_Table+" (id serial PRIMARY KEY,topicsref VARCHAR ( 100 ) , owner VARCHAR ( 100 ) ,project VARCHAR ( 100 )  );"
cursor.execute(sqlCreateTable)
postgresConnection.commit()
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
sqlGetTableList = "INSERT INTO topicsname(topicsref, owner,project) VALUES ('', '', '') ;"
cursor.execute(sqlGetTableList)
print("exit form code")
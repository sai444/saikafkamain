import psycopg2
postgresConnection    = psycopg2.connect("dbname=todo user=iotmax password='iotmax'")
cursor                = postgresConnection.cursor()
name_Table            = "maintopicstable"


myname = "sai_mynew_15_sasiub"

sqlGetTableList = "SELECT * FROM maintopicstable ;"
cursor.execute(sqlGetTableList)
tables = cursor.fetchall()


for table in tables:
	
    #print(type(table))
	if str(table[1]) in myname:
		print("query found")
		print('topicname = ',myname , 'ref = ' ,table[1], 'project = ' ,table[2],'owner = ' ,table[3])
	

import mysql.connector, csv
from mysql.connector import errorcode

try:
	
	# ******************************** 
	# Add test data
	# ******************************** 
	cnx = mysql.connector.connect(user='user', database='database')
	
	insert_sql = (
		"LOAD DATA INFILE '%s' "
		"INTO TABLE %s "
		"FIELDS TERMINATED BY ',' "
		"LINES TERMINATED BY '" 
		r"\n"
		"' "
		"IGNORE 1 ROWS"
		)
	
	# ******************************** 
	# Extract data from database 
	# ******************************** 
	file_name = r'C:/Destination'
	table_name = 'schema.table'
	
	cursor1 = cnx.cursor()
	extract_sql = ("SELECT * FROM %s" % table_name) 
	cursor1.execute(extract_sql)
	
	with open(file_name, 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor1.description]) # write headers
		csv_writer.writerows(cursor1)
	
	cnx.commit()
	csv_file.close()
	
	#cursor1.execute('DELETE FROM %s'%table_name) #testing only
	#cnx.commit() #testing only
	
	cursor1.close()
	
	# ******************************** 
	# Write data to database 
	# ******************************** 
	cursor2 = cnx.cursor()
	cursor2.execute(insert_sql % (file_name,table_name))
	cnx.commit()
	cursor2.close()
	
	# ******************************** 
	# Close connections 
	# ******************************** 
	cnx.close()
	
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)
else:
  cnx.close()
import mysql.connector, csv
from mysql.connector import errorcode

# ---------------------------------------------------------- 
# This script shows you how to connect to a MySQL database, 
# extract data from the database, then write it back to the
# database as well
# ---------------------------------------------------------- 

# ******************************** 
# General variables
# ******************************** 
file_name = r'C:/Destination'
table_name = 'schema.table'

try:
	# ******************************** 
	# Connect to MySQL database
	# ******************************** 
	cnx = mysql.connector.connect(user='user', database='database')
	
	# ******************************** 
	# Extract data from database 
	# ******************************** 
	extract_sql = ("SELECT * FROM %s" % table_name)
	
	cursor1 = cnx.cursor()
	cursor1.execute(extract_sql)
	
	with open(file_name, 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor1.description]) # write headers
		csv_writer.writerows(cursor1)
	
	cnx.commit()
	csv_file.close()
	cursor1.close()
	
	# ****************************************  
	# Remove original data - ONLY AS DESIRED
	# **************************************** 
	#cursor2 = cnx.cursor()
	#cursor2.execute('DELETE FROM %s'%table_name)
	#cnx.commit()
	#cursor2.close()
	
	# ******************************** 
	# Write data to database 
	# ******************************** 
	insert_sql = (
		"LOAD DATA INFILE '%s' "
		"INTO TABLE %s "
		"FIELDS TERMINATED BY ',' "
		"LINES TERMINATED BY '" 
		r"\n"
		"' "
		"IGNORE 1 ROWS"
		)
	
	cursor3 = cnx.cursor()
	cursor3.execute(insert_sql % (file_name,table_name))
	cnx.commit()
	cursor3.close()
	
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
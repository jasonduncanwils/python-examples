import pyodbc, csv

try:
	cnx = pyodbc.connect(r'Driver={SQL Server};Server=server;Database=database;Trusted_Connection=yes;')
	file_name = r'C:/Destination'
	
	cursor1 = cnx.cursor()
	
	sql = ("add SQL")
	
	cursor1.execute(sql)
	
	with open(file_name, 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor1.description]) # write headers
		csv_writer.writerows(cursor1)
	
	cnx.commit()
	
	cursor1.close()
	
except pyodbc.Error as err:
		print(err)
else:
  cnx.close()
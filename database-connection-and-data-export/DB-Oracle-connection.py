import cx_Oracle, csv
from sys import argv
import getpass

# argv specifies the expected input parameters when calling the script
script, exec_date, output_folder = argv

# set some general variables
exec_date = int(exec_date)
file_name = output_folder + r'/filename'

# get user to input their user name and password
username = input('Enter database username: ')
pswd = getpass.getpass('Enter Password:')

try:
	
	# define connection to Oracle database (this could be passed in as well)
	cnx = cx_Oracle.connect(username + r'/' + pswd + r'@server:port/SID')
	
	# execute SQL to select data
	cursor1 = cnx.cursor()
	sql = ("""
	[add SQL here]
	""" % (exec_date))
	
	cursor1.execute(sql)
	
	# write out file based on SQL results
	with open(file_name, 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor1.description]) # write headers
		csv_writer.writerows(cursor1)
	cnx.commit()
	
	# close cursor
	cursor1.close()
	
except cx_Oracle.Error as err:
	print(err)
	
else:
	cnx.close()
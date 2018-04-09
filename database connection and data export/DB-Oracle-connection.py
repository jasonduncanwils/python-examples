import cx_Oracle, csv
from sys import argv
import getpass

script, exec_date, output_folder = argv
exec_date = int(exec_date)

username = input('Enter database username: ')
pswd = getpass.getpass('Enter Password:')

try:

	cnx = cx_Oracle.connect(username + r'/' + pswd + r'@server:port/SID')
	file_name = output_folder + r'/folder'
	
	cursor1 = cnx.cursor()
	sql = ("""
	[add SQL here]
	""" % (exec_date))
	
	cursor1.execute(sql)
	
	with open(file_name, 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		csv_writer.writerow([i[0] for i in cursor1.description]) # write headers
		csv_writer.writerows(cursor1)
	
	cnx.commit()
	cursor1.close()
	
except cx_Oracle.Error as err:
	print(err)
	
else:
	cnx.close()
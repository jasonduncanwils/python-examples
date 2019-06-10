import csv, xml.etree.cElementTree as et
from sys import argv

script, source_folder, output_folder = argv

input_file_name = source_folder + r'newfile.csv'
delimiter = ','
quote_character = '"'

def rows_as_dicts(csv_reader, colnames):
    for row in csv_reader:
        yield dict(zip(colnames, row))

with open(input_file_name, 'r') as csv_fp:
	csv_reader = csv.reader(csv_fp, delimiter=delimiter, quotechar=quote_character)
	colnames = csv_reader.__next__()
	
	for row in rows_as_dicts(csv_reader, colnames):
		
		car = et.Element("car", dateTimeTagFormat="xsd:strict")
		vin = et.SubElement(car, "vin").text = row["VIN"]
		make = et.SubElement(car, "make").text = row["MAKE"]
		model = et.SubElement(car, "model").text = row["MODEL"]
		interior = et.SubElement(car, "interior")
		interiortype = et.SubElement(interior, "interiortype").text = row["INTERIORTYPE"]
		interiorcolor = et.SubElement(interior, "interiorcolor").text = row["INTERIORCOLOR"]
		
		#write out xml tree as a row in file
		xmltree = et.ElementTree(car)
		output_file_name = output_folder + 'CAR-' + row["VIN"] + r'.xml'
		xmltree.write(output_file_name)
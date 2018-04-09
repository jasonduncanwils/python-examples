from sys import argv
script, filename = argv

dna_4_letters = ['g','a','t','c']
dna_list = []

print '-' * 80 

print "Filename:",filename

print '-' * 80 

my_test_file = open(filename).read()
print my_test_file

print '-' * 80 

my_test_file.replace(" ", "")
for line in my_test_file:
	for char in line:
		if char in dna_4_letters:
			dna_list.append(char)

print dna_list

print '-' * 80 

print ''.join(dna_list)

print '-' * 80 
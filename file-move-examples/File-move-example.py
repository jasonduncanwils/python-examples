import shutil, sys, time, os

# general variables
src = 'C:\Source'
dst = 'C:\Destination'
now = time.time()
print (now)

# iterate through files to move them
for path, dirs, files in os.walk(src):
	for f in files:
		f = os.path.join(path, f)
		try:
			shutil.move(f, dst)
		except os.error:
			continue
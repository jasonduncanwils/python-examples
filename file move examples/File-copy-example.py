import shutil, sys, time, os
src = 'C:\Source'
dst = 'C:\Destination'

now = time.time()
print (now)
for path, dirs, files in os.walk(src):
	for f in files:
		f = os.path.join(path, f)
		try:
			shutil.copy(f, dst)
		except os.error:
			continue
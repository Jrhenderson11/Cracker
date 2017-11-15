import crypt
import sys
import os

from os import listdir
from os.path import isfile, join, dirname

def crack(password):

	print("cracking " + password)
	groups = password.split('$')
	salt = '$'.join(groups[:3])
	result = '$'.join(groups[3:])
	print("salt: " + salt)
	print("password: " + result)

#print (crypt.crypt("PASSWORD", crypt.mksalt(crypt.METHOD_MD5)))
fileList = sys.argv
fileName = fileList[1]
file = open(fileName, "r")
text = file.read()
file.close()

#print(text)
print("Useful lines:")
useful = []


#find users
lines = text.split("\n")
for line in lines:
	if (len(line.split(":"))>1 and not (line.split(":")[1] in ["!", "*"])):
		useful.append(line)

for line in useful:	
	#crack password
	crack(line.split(":")[1])




#get salt
#START CRACKING BASTARDS
#print (crypt.crypt("crappassword", "$6$Ez7LodYS$"))
#!/usr/bin/python

import random, sys, string

#We need 3 params
#Script-name, input-file, output-file
if len(sys.argv) <> 3:
	print "Usage: python obfuscator.py inFile.vbs outFile.vbs"
	sys.exit()
	
#Splitter is set to be the "*" symbol,
#since we are not using it in obfuscation
splitter = str(chr(42))

#Randomly capitalize each character
def randCapitalization(characters):
	capicharacter = ""
	for character in characters:
		lowup = random.randrange(0,2)
		if lowup == 0:
			capicharacter += character.upper()
		if lowup == 1:
			capicharacter +=  character.lower()
	return capicharacter


#Random function names
NUM_OF_CHARS = random.randrange(5, 60)
pld = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
array = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
temp = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))

#Random Sub names
subOne = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))
subTwo = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(NUM_OF_CHARS))

#Function to fill encBody variable
#with the obfuscated content
def obfu(body):
	encBody = ""
	for i in range(0, len(body)):
		if encBody == "":
			encBody += expr(ord(body[i]))
		else:
			encBody += "*" + expr(ord(body[i]))
	return encBody

#Random mathematical expression decision
def expr(char):
	range = random.randrange(100, 10001)
	exp = random.randrange(0, 3)

	if exp == 0:
		print "Char " + str(char) + " -> " + str((range+char)) + "-" + str(range)
		return str((range+char)) + "-" + str(range)
	if exp == 1:
		print "Char " + str(char) + " -> " + str((char-range)) + "+" + str(range)
		return str((char-range)) + "+" + str(range)
	if exp == 2:
		print "Char " + str(char) + " -> " + str((char*range)) + "/" + str(range)
		return str((char*range)) + "/" + str(range)

#Open the source and destination files
clear_text_file = open(sys.argv[1], "r")
obfuscated_file = open(sys.argv[2], "w")

#Write to destination file
obfuscated_file.write(randCapitalization("Dim " + pld + ", " + array + ", " + temp) + "\n")
obfuscated_file.write(randCapitalization("Sub " + subOne) + "\n")
obfuscated_file.write(randCapitalization(pld + " = ") + chr(34) + obfu(clear_text_file.read()) + chr(34) + "\n")
obfuscated_file.write(randCapitalization(array + " = Split(" + pld + ", chr(eval(") + obfu(splitter) + ")))\n")
obfuscated_file.write(randCapitalization("for each " + x + " in " + array) + "\n")
obfuscated_file.write(randCapitalization(temp + " = " + temp + " & chr(eval(" + x) + "))\n")
obfuscated_file.write(randCapitalization("next") + "\n")
obfuscated_file.write(randCapitalization(subTwo) + "\n")
obfuscated_file.write(randCapitalization("End Sub") + "\n")
obfuscated_file.write(randCapitalization("Sub " + subTwo) + "\n")
obfuscated_file.write(randCapitalization("eval(execute(" + temp) + "))\n")
obfuscated_file.write(randCapitalization("End Sub") + "\n")
obfuscated_file.write(randCapitalization(subOne) + "\n")

#Close file handles before exit
clear_text_file.close()
obfuscated_file.close()

print "Done!"

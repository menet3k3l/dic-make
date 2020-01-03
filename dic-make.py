#!/bin/python3

import sys
import itertools

print("dic-make v0.0")
print(90*"-")
print("Write a bunch of keywords to generate a password dictionary.\nThe program will automatically make all combinations of uppers and lowers, with the most common numbers.\nNumbers like birthday have to be manually put in.")
print(90*"-")
print("\nIdeas: pets, names, streets, cities, favourite bands/artists, favourite activities, company, sports, sports players...Be creative!\n")
print(90*"-")

number = -1
caps = -1


def mix_lists(b,c,d):
	a = b + c + d
	return a


if ("-h" in sys.argv) and (len(sys.argv) == 2):
	print("Syntax: ")
	print("python3 dic-make.py [options]\n")
	print("-n (#) = add numbers after keywords, # - how many numbers (default 9 = 0 - 9), max 9999\n")
	print("-c (#) = add caps, 1 - first letters upper, 2 - all combinations, (default 1)\n")
	print("-h     = help")
	sys.exit()

if "-n" in sys.argv:
	test = False
	if sys.argv[-1] == "-n":
		number = 9
		test = True
	elif not test:
		i = 0
		position = 0 #position of # in "-n 9999"
		for i in range(len(sys.argv)):
			if sys.argv[i] == "-n":
				position = i+1
		try:
			if int(sys.argv[position]) > 9999:
				print("-n (#) has to be 0 - 9999...exiting...")
				sys.exit()
			else:
				number = int(sys.argv[position])
		except:
			if "-c" not in sys.argv[position]:
				print("Error: invalid command, use \"-h\" for syntax")
				sys.exit()
			else:			
				number = 9

if "-c" in sys.argv:
	test = False
	if sys.argv[-1] == "-c":
		caps = 1
		test = True
	elif not test:
		i = 0
		position = 0 #position of # in "-c 1"
		for i in range(len(sys.argv)):
			if sys.argv[i] == "-c":
				position = i+1
		try:
			if int(sys.argv[position]) > 2:
				print("-c (#) has to be 1 or 2...exiting...")
				sys.exit()
			else:
				caps = int(sys.argv[position])
		except:
			if "-n" not in sys.argv[position]:
				print("Error: invalid command, use \"-h\" for syntax")
				sys.exit()
			else:			
				caps = 1
		
if len(sys.argv) == 1:
	number = -1
	caps = -1

elif (len(sys.argv) > 1) and not (("-h" in sys.argv) or ("-n" in sys.argv) or ("-c" in sys.argv)):
	print("Error: invalid command, use \"-h\" for syntax")
	sys.exit()

#print("Argument List: {}".format(sys.argv))
#print("Number: {}\nCaps: {}\n".format(number,caps))

print("To stop entering new words, type either -e or --exit")
print("To print your keywords so far, type either -p or --print")
print("To delete something from your keywords, type -d [keyword] "" or --delete [keyword] """)
print("\n")
filename = input("Enter filename: ")
print("\n")
print("Enter keywords now:")

keywords = []

while True:
	word = input("> ")

	if (word == "-e") or (word == "--exit"):
		print("\nExiting...\n")
		break

	elif (word == "-p") or (word == "--print"):
		print("\nPrinting your keywords...\n")
		print(keywords)
		print("\n")

	elif ("-d" in word) or ("--delete" in word):
		split = word.split()
		if split[1] in keywords:
			print("Deleting \"{}\"".format(split[1]))
			keywords.remove(split[1])
		elif not (split[1] in keywords):
			print("There's no \"{}\" in keywords.".format(split[1]))
	
	elif word == "":
		continue

	else:
		keywords.append(word)

keynumbers = ["0123", "1234", "123456", "0123456", "987654", "123456789"]

print("Enter keynumbers now:\n")

while True:
	word = input("> ")

	if (word == "-e") or (word == "--exit"):
		print("\nExiting application now\n")
		break

	elif (word == "-p") or (word == "--print"):
		print("\nPrinting your keynumbers...\n")
		print(keynumbers)
		print("\n")

	elif ("-d" in word) or ("--delete" in word):
		split = word.split()
		if split[1] in keynumbers:
			print("Deleting \"{}\"".format(split[1]))
			keynumbers.remove(split[1])
		elif not (split[1] in keynumbers):
			print("There's no \"{}\" in keynumbers.".format(split[1]))
	
	elif word == "":
		continue

	else:
		keynumbers.append(word)
	

#generating all combinations of lower and upper

print("\nGenerating dictionary now...\n")

if caps == 1:
	capsList = []
	for keyword in keywords:
		if keyword[0].islower():
			keyword = keyword[0].upper() + keyword[1:]
			capsList.append(keyword)
		elif keyword[0].isupper():
			keyword = keyword[0].lower() + keyword[1:]
			capsList.append(keyword)
	keywords = keywords + capsList

elif caps == 2:
	capsList = []
	for keyword in keywords:
		x = list(map(''.join, itertools.product(*zip(keyword.upper(), keyword.lower()))))
		x.remove(keyword)
		capsList = capsList + x
	keywords = keywords + capsList

newList = []

for keyword in keywords:
	for keynumber in keynumbers:
		newList.append(keyword+keynumber)


if number > 0:
	addingList = []
	for keyword in keywords:
		for i in range(number+1):
			if number < 10:
				x = "{0:01}".format(i)
				addingList.append(keyword+x)
			elif (number >= 10) and (number < 100):
				x = "{0:01}".format(i)
				addingList.append(keyword+x)
				if i < 10:
					x = "{0:02}".format(i)
					addingList.append(keyword+x)
			elif (number >= 100) and (number < 1000):
				x = "{0:01}".format(i)
				addingList.append(keyword+x)
				if i < 10:
					x = "{0:02}".format(i)
					addingList.append(keyword+x)
					x = "{0:03}".format(i)
					addingList.append(keyword+x)
				elif (i >= 10) and (i < 100):
					x = "{0:03}".format(i)
					addingList.append(keyword+x)
			
	keywords = keywords + addingList

	

f = open(filename, "a")

mixed = mix_lists(keywords, keynumbers, newList)

for i in range(len(mixed)):
	f.write(mixed[i])
	f.write("\n")

f.close()

#menet3k3l 2020

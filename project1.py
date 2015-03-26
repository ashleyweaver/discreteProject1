import random

def fileToString(fileName) :
	f = open(fileName, "r")
	fileString = f.read()
	return fileString

def stringToFile(fileString) :
	fileName = open("newLetter.txt", "w")
	fileName.write(fileString)
	fileName.close()
	return fileName

def replaceName(letter, oldName, newName) :
	newLetter = letter.replace(oldName, newName)
	return newLetter

def replaceWord(letter, wordListString, word) :
	wordList = wordListString.split("\n")
	newLetter = letter.replace(word, random.choice(wordList))
	return newLetter

def replacePhrase(letter, oldPhrase, newPhrase) :
	newLetter = letter.replace(oldPhrase, newPhrase)
	return newLetter

def encode(letter, secretPhrase) :
	letterWords = letter.split()
	binarySpaces = []
	codedLetter = ""
	secretPhraseLower = secretPhrase.lower()
	while len(secretPhraseLower) > 0 :
		l = secretPhraseLower[:1]
		secretPhraseLower = secretPhraseLower[1:]
		if l.isalpha() :
			binList = []
			bin = '{0:05b}'.format(ord(l) - ord('a'))
			print bin
			for b in bin :
				if b == '0' :
					binList.append(" ")
				elif b == '1' :
					binList.append("  ")
			binarySpaces.append(binList)
	
	binarySpaces.append(["  ", "  ", "  ", "  ", "  "])
	if len(letterWords) < (len(binarySpaces) * 5) + 1 :
		print "Secret phrase too long for this letter."
	else :
		codedLetter += letterWords.pop(0)
		for b in binarySpaces :
			while len(b) > 0 :
				codedLetter += b.pop(0)
				codedLetter += letterWords.pop(0)
		while len(letterWords) > 0 :
			codedLetter += " "
			codedLetter += letterWords.pop(0)
		return codedLetter

def decode(codedLetter) :
	binary = ""
	i = -1
	for l in codedLetter :
		if l.isspace() == False :
			if i > -1 :
				binary += str(i)
				i = -1
		else :
			i += 1
	
	secretPhrase = ""
	binList = [binary[i:i+5] for i in range(0, len(binary), 5)]

	for b in binList :
		if b == "11111" :
			break
		else :
			secretPhrase += chr(int(b, 2) + ord('a'))

userInput = 0
while userInput != 5:
	print ("1: Replace student's name")
	print ("2: Replace specific word")
	print ("3: Replace phrase")
	print ("4: Encode\decode secret message")
	print ("5: Quit")
	userInput = input("Enter your choice: ")
	if userInput == 1 :
		letterFile = input("Enter the letter file name: ")
		oldName = input("Enter the old name: ")
		newName = input("Enter the new name: ")
		newLetter = replaceName(fileToString(letterFile), oldName, newName)
		print newLetter
		yn = input("Would you like to save? (y/n)")
		if yn == "y" :
			newLetterFile = stringToFile(newLetter)
		else :
			break
	elif userInput == 2 :
		letterFile = input("Enter the letter file name: ")
		wordListFile = input("Enter the word list file name: ")
		oldWord = input("Enter the old word/phrase: ")
		newLetter = replaceWord(fileToString(letterFile), fileToString(wordListFile), oldWord)
		print newLetter
		yn = input("Would you like to save? (y/n)")
		if yn == "y" :
			newLetterFile = stringToFile(newLetter)
		else :
			break
	elif userInput == 3 :
		letterFile = input("Enter the letter file name: ")
		oldPhrase = input("Enter the old phrase: ")
		newPhrase = input("Enter the new phrase: ")
		newLetter = replaceName(fileToString(letterFile), oldPhrase, newPhrase)
		print newLetter
		yn = input("Would you like to save? (y/n)")
		if yn == "y" :
			newLetterFile = stringToFile(newLetter)
		else :
			break
	elif userInput == 4 :
		print ("1: Encode a letter")
		print ("2: Decode a letter")
		userAnswer = input("Enter your choice: ")

		if userAnswer == 1 :
			letterFile = input("Enter the letter file name: ")
			secretPhrase = input("Enter the secret phrase: ")
			newLetter = encode(fileToString(letterFile), secretPhrase)
			print newLetter
			yn = input("Would you like to save? (y/n)")
			if yn == "y" :
				newLetterFile = stringToFile(newLetter)
			else :
				break
		elif userAnswer == 2 :
			letterFile = input("Enter the letter file name: ")
			newLetter = decode(fileToString(letterFile))
			print newLetter
			yn = input("Would you like to save? (y/n)")
			if yn == "y" :
				newLetterFile = stringToFile(newLetter)
			else :
				break
		else :
			print ("Invalid input.")
			break
	elif userInput == 5 :
		print "Good-bye."
		break
	else :
		print ("Invalid input.")
		break			
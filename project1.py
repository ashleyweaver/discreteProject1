import random

def fileToString(fileName) :
	fileString = fileName.read()
	return fileString

def stringToFile(fileString) :
	fileName = open("newLetter.txt", "w")
	fileName.write(fileString)
	fileName.close()
	return fileName

def replaceName(letter, oldName, newName) :
	newLetter = letter.replace(oldName, newName)
	return newLetter

def replaceWord(letter, wordList, word) :
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
		e = secretPhraseLower[:1]
		secretPhraseLower = secretPhraseLower[1:]
		if e.isalpha() :
			binList = []
			bin = '{0:05b}'.format(ord(e) - ord('a'))
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



print encode("""This is my test letter. I need to type a lot of words here. 
				I'm not good at typing words. Words, words, words. This is the 
				end sentence. Goodbye, cruel world. Adding a few more words 
				because I can't count.""", "test it")
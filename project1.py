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


testString = "Ashley likes the sexy men"
adjList = ["hot", "nerdy", "cute"]
print testString
print replaceName(testString, "Ashley", "Nick")
print replaceWord(testString, adjList, "sexy")
print replacePhrase(testString, "the sexy men", "hot women with tattoos")
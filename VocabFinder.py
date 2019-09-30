import sys
from PyDictionary import PyDictionary
dictionary=PyDictionary()

def FindWord(x):
	defi = []
	for y in x:
		defi.append(dictionary.meaning(y))
	return defi









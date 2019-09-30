from PyDictionary import PyDictionary
pydic = PyDictionary()

class Vocab:
	def __init__(self, word, definition=None, syn=None, antm=None):
		self.word = word
		self.definition = definition
		self.syn = syn
		self.antm= antm



class PyDic(Vocab):
	def __init__(self, word, definition=None, syn=None, antm=None):
		self.word = word
		self.definition = pydic.meaning(word)
		self.syn= pydic.synonym(word)
		self.antm= pydic.antonym(word)


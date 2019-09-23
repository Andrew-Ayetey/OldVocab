from VocabFinder import *
import sqlite3
import pandas as pd
pd.set_option('display.max_colwidth', -1)
# pd.set_option('display.max_columns', None) 


conn = sqlite3.connect('VBtest.db')

c = conn.cursor()

# print "".join(str((dictionary.meaning('weft').values())))







# c.execute("""CREATE TABLE Definitions (
# 	word text UNIQUE,
#  	definition text UNIQUE
#   	)""")

def VBinsert(x):
	defin = str(dictionary.meaning(x))
	if defin == 'None':
		return 'No definition'
	else:
		pass
	
	c.execute("INSERT INTO Definitions VALUES (?, ?)", (x, defin))
	conn.commit()

	return







# c.execute("SELECT * FROM Definitions")
# print pd.read_sql_query("SELECT * FROM Definitions", conn)

# w = ['scurrilous']

# for x in w:
# 	VBinsert(x)


conn.commit()

c.execute("SELECT * FROM Definitions")
print (pd.read_sql_query("SELECT * FROM Definitions", conn))

conn.close()


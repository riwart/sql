import sqlite3

conn = sqlite3.connect("newnum.db")

c = conn.cursor()

prompt	=	"""
Select	the	operation	that	you	want	to	perform	[1-5]:
1.	Average
2.	Max
3.	Min
4.	Sum
5.	Exit
"""

while True:
	# get user input
	x = input(prompt)
	
	# if user enters any choice from 1-4
	if x in set(["1", "2", "3", "4"]):
		# parse the corresponding operation text
		operation = {1:'AVG', 2:'MAX', 3:'MIN', 4:'SUM'}[int(x)]
		
		# retrieve data
		c.execute("SELECT {}(num) FROM numbers".format(operation))
		
		# fetchone() retrieves one record from the query (there is only one record available)
		get = c.fetchone()
		
		# output result to screen
		print(operation + ": %f" % get[0])
	
	elif x == "5":
		print("EXIT")
		
		# exit loop
		break


names = ["Lewis", "Ronald", "Bingstrom", "Badjen"]
places = ["1st", "3rd", "2nd", "4th"]


def iterate(list):
	for item in list:
		print item
		
def print_place(names, places):
	for i in range (0, len(names)):
		print names[i] , "finished" , places[i]
		
def congrats (names, places):
	for i in range (0, len(names)):
		if places[i] == "1st"
			print "You're okay"
		elif places[i] == "2nd"
			print "second place is first loser"
		else places[i] == "3rd"
			print "git gud"
			

print_place(names, places)
congrats(names, places)
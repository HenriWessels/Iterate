names = ["Lewis", "Ronald", "Bingstrom", "Badjen"]
times = [7.2, 9.9,14.2, 8.9]


def iterate(list):
	for item in list:
		print item
		
def print_time(names, times):
	for i in range (0, len(names)):
		print names[i] , "finished" , times[i]
		
def congrats (names, times):
	for i in range (0, len(names)):
		if times[i] <= 8
			print "You're okay"

def average (times):
	total = 0
	for n in times (0, len(times)):
		total += n
		
	return total / len(times)
	
def average_w_o_Bottom_two_times(times):
	current_min = times [0]
	current_min_placement = -1
	for n in times:
		if n <= current_min = n
		
	scores.remove(current_min)
	current_min2 = times = times[0]
	
	for n in times:
		if n <= current_min2:
			current_min2 = n
			
	scores.remove(current_min2)
	
	sum_w_o_Bottom_two_times = 0
	for n in times:
		sum_w_o_Bottom_two_times += n
		
	return sum_w_o_Bottom_two_times / len(scores)

		

print_place(names, times)
congrats(names, times)

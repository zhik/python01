num_list = []

while True:
	num = raw_input("Enter a number or 'done': ")

	#check if the input is done 
	if num == "done":

	#check if the list is empty
		if num_list != []:
			print("here are your numbers")
			break
		else:
			print("there are no numbers in the list")
			continue
	#check if the input is a float/num
	try:
		num = float(num)
	except:
		print("you didn't enter a number or 'done'")
		continue
	#add number to list
	num_list.append(num)

print "this is your list", num_list
largest	= max(num_list)
smallest = min(num_list)
print "Maximum number is: ", largest
print "Minimum number is: ", smallest



# Write a program to read through the mbox-short.txt and figure out the distribution
# by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time 
# and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts,
#  sorted by hour as shown below.
name = raw_input("Enter file:")
if len(name) < 1 : 
	name = "mbox-short.txt"
handle = open(name)

dictofhours = dict()
for line in handle:
	line = line.strip()
	#find the hours by looking for the first ":" then -2 
	if line.startswith("From "):
		hour_place = line.find(":") 
		hour = line[hour_place -2:hour_place]
		#add to dict, and count the amount of instances 
		dictofhours[hour] = dictofhours.get(hour, 0) + 1

# #this is if you want to sort by the highest counts
# print sorted([(value, key) for key, value in dictofhours.items()],reverse=True)

#this is for if you want to sort by hours(12 hour format)
for key,value in sorted(dictofhours.items()):
	#if it's over 12 hours then -12 and add pm
	if int(key) > 12:
		ap_key = str(int(key) - 12)
		ap_time = ap_key + "  pm "
	#if it's 09 and under take out the 0 because it's ugly and add am
	elif key[0] == "0":
		ap_key = key[1]
		ap_time = ap_key + "  am "
	#10-12 add am
	else:
		ap_key = str(key)
		ap_time = ap_key + " am"
	print dictofhours[key], "@", ap_time
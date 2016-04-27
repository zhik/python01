
# Write a program to read through the mbox-short.txt and figure out the distribution
#  by hour of the day for each of the messages. 
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
	if line.startswith("From "):
		hour_place = line.find(":") 
		hour = line[hour_place -2:hour_place]
		#add to dict, and count the amount of instances 
		dictofhours[hour] = dictofhours.get(hour, 0) + 1


for key,value in dictofhours.items():
	if int(key) > 12:
		us_key = str(int(key) - 12)
		us_time = us_key + " pm"
	else:
		us_key = str(key)
		us_time = us_key + "am"
	print us_time, dictofhours[key]
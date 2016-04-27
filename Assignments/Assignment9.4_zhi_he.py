# Write a program to read through the mbox-short.txt and figure out who has 
# the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines
# as the person who sent the mail. 
# The program creates a Python dictionary that maps the
# sender's mail address to a count of the number of times they 
# appear in the file. 
# After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.

from_dict = dict()
	
name = raw_input("Enter file:")
if len(name) < 1 :
	name = "mbox-short.txt"
handle = open(name)

for line in handle:
	line = line.strip()

	#find all lines with From 
	if line.startswith("From "):
		#find the ending of the email
		endofword = line.find(' ', line.find(' ') + 1)
		#find the email using the spaces
		from_word = line[line.find(' ')+1:endofword]
		#add to dict, and count the amount of instances 
		from_dict[from_word] = from_dict.get(from_word, 0) + 1

#find the biggest
from_biggest = None	
from_count = None
for word,count in from_dict.items():
	if from_biggest == None or count > from_count:
		from_biggest = word
		from_count = count

print "largest is", from_biggest, "at" ,from_count
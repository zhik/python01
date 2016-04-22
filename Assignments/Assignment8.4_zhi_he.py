# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. 
# For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in alphabetical order.

#fname = raw_input("Enter file name: ")
fh = open('romeo.txt')
lst = list()

#clean lines and split word
for line in fh:
	word_lst = line.rstrip().split()

#test if word is not in the list, so it can be added 
#also make sure it's lowercase so it can be sorted
	for word in word_lst:
		if word not in lst:
			lst.append(word.lower())

#sort the list
print sorted(lst)


